"""Script to run end-to-end evaluation on the benchmark.
Utils and basic architecture credit to https://github.com/web-arena-x/webarena/blob/main/run.py.
"""
import argparse, datetime, json, logging, os, shutil, sys
from tqdm import tqdm
import lib_run_single
from typing import List, Tuple, Dict, Any, Optional
from desktop_env.envs.desktop_env import DesktopEnv
from mm_agents.agent import PromptAgent

#  Logger Configs {{{ #
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
os.makedirs("logs", exist_ok=True)
datetime_str: str = datetime.datetime.now().strftime("%Y%m%d@%H%M%S")
file_handler = logging.FileHandler(os.path.join("logs", "normal-{:}.log".format(datetime_str)), encoding="utf-8")
debug_handler = logging.FileHandler(os.path.join("logs", "debug-{:}.log".format(datetime_str)), encoding="utf-8")
stdout_handler = logging.StreamHandler(sys.stdout)
file_handler.setLevel(logging.INFO)
debug_handler.setLevel(logging.DEBUG)
stdout_handler.setLevel(logging.INFO)
formatter = logging.Formatter(
    fmt="\x1b[1;33m[%(asctime)s \x1b[31m%(levelname)s \x1b[32m%(module)s/%(lineno)d-%(processName)s\x1b[1;33m] \x1b[0m%(message)s")
pure_formatter = logging.Formatter(fmt="[%(asctime)s %(levelname)s %(module)s/%(lineno)d]: %(message)s")
file_handler.setFormatter(formatter)
debug_handler.setFormatter(formatter)
stdout_handler.setFormatter(formatter)
stdout_handler.addFilter(logging.Filter("desktopenv"))
logger.addHandler(file_handler)
logger.addHandler(debug_handler)
logger.addHandler(stdout_handler)
logger = logging.getLogger("desktopenv.experiment")


ALL_DOMAINS = ['excel', 'servicenow', 'jupyter', 'dbt', 'airflow', 'dagster', 'airbyte', 'snowflake', 'bigquery', 'superset', 'metabase']


def config() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run end-to-end evaluation on the benchmark")

    # environment config
    parser.add_argument('-p', "--path_to_vm", type=str, help="path to the VM executable .vmx file, if None, automatically find the VM in vm_data/ folder")
    parser.add_argument('-s', "--snapshot_name", type=str, default="init_state", help="Snapshot name to use (overwrite snapshot in each example config)")
    parser.add_argument("--headless", action="store_true", help="Run in headless machine")
    parser.add_argument(
        "--action_space",
        choices=[
            "pyautogui",
            "computer_13"
        ],
        default="pyautogui",
        help="Action space to use for the agent"
    )
    parser.add_argument(
        "--observation_space",
        choices=[
            "screenshot",
            "a11y_tree",
            "screenshot_a11y_tree",
            "som"
        ],
        default="som",
        help="Observation space to use for the environment",
    )
    parser.add_argument("--sleep_after_execution", type=float, default=0.5)
    parser.add_argument("--max_steps", type=int, default=15, help="Maximum number of steps for each example, this can be altered dynamically according to field `action_number` in the example config")

    # agent config
    parser.add_argument("--max_trajectory_length", type=int, default=3, help='maximum length of interaction history to provide to the agent')
    parser.add_argument("--a11y_tree_max_tokens", type=int, default=5000, help='maximum length of interaction history to provide to the agent')

    # llm config
    parser.add_argument('-m', "--model", type=str, default="gpt-4o-2024-05-13", help="LLM model to use for the agent")
    parser.add_argument("--temperature", type=float, default=0.5)
    parser.add_argument("--top_p", type=float, default=0.9)
    parser.add_argument("--max_tokens", type=int, default=1500)

    # example config
    parser.add_argument('-e', "--example", type=str, default=os.path.join('evaluation_examples', 'test_one.json'), help="JSON dict containing example ids to run")
    parser.add_argument("--exclude_account", action='store_true', help="Whether to use RAG for the agent")
    parser.add_argument("--execution_feedback", action='store_true', help="whether to use execution feedback for the agent")
    parser.add_argument("--rag", action='store_true', help="Whether to use RAG for the agent")
    parser.add_argument("--rag_topk", type=int, default=4, help="Top k to use for RAG")
    parser.add_argument("--rag_filename", type=str, default="retrieved_chunk_size_512_chunk_overlap_20_topk_4_embed_bge-large-en-v1.5.txt", help="RAG retrieved context file name")
    parser.add_argument("--domains", choices=ALL_DOMAINS + ['all'], nargs='+', default=["all"], help="Application names list to filter examples")

    # logging related
    parser.add_argument("--result_dir", type=str, default="./results")
    parser.add_argument("--from_scratch", action="store_true", help="Run from scratch, ignore existing results")
    args = parser.parse_args()

    if args.observation_space == 'som':
        assert args.action_space == 'pyautogui', "SOM only supports pyautogui action space"
    return args


def get_retrieved_context(config_path: str, topk: int = 4, file_name: str = "retrieved_chunk_size_512_chunk_overlap_20_topk_4_embed_bge-large-en-v1.5.txt") -> str:
    context_path = os.path.join(os.path.dirname(config_path), file_name)
    if os.path.exists(context_path):
        with open(context_path, "r", encoding="utf-8") as f:
            context = f.read().strip()
        if context.strip() == "": return None
        splits = context.split("Documentation Source:")
        if len(splits) > topk + 1: # the first is ""
            return "Documentation Source:".join(splits[:topk + 1])
        return context
    raise ValueError(f"Retrieved context not found under {os.path.dirname(config_path)}")


def test(args: argparse.Namespace, test_all_meta: List[dict]) -> dict:
    scores = {}
    logger.info("Args: %s", args)
    env = DesktopEnv(
        path_to_vm=args.path_to_vm,
        snapshot_name=args.snapshot_name,
        action_space=args.action_space,
        headless=args.headless,
        require_a11y_tree=args.observation_space in ["a11y_tree", "screenshot_a11y_tree", "som"]
    )

    agent = PromptAgent(
        platform="ubuntu",
        model=args.model,
        max_tokens=args.max_tokens,
        action_space=args.action_space,
        observation_space=args.observation_space,
        execution_feedback=args.execution_feedback,
        screen_size=env.vm_screen_size,
        temperature=args.temperature,
        max_trajectory_length=args.max_trajectory_length,
        a11y_tree_max_tokens=args.a11y_tree_max_tokens
    )

    for example in tqdm(test_all_meta, desc="Example", leave=False):
        domain, eid = example['domain'], example['id']
        if domain not in scores:
            scores[domain] = []
        config_file, result_dir = example['config'], example['result']
        with open(config_file, "r", encoding="utf-8") as f:
            example = json.load(f)

        if args.rag: example['context'] = get_retrieved_context(config_file, args.rag_topk, file_name=args.rag_filename)
        else: example['context'] = None

        root_logger = logging.getLogger()
        example_handler = logging.FileHandler(os.path.join(result_dir, "result-{:}.log".format(datetime_str)), encoding="utf-8")
        example_handler.setLevel(logging.INFO)
        example_handler.setFormatter(pure_formatter)
        example_handler.addFilter(logging.Filter("desktopenv"))
        root_logger.addHandler(example_handler)

        logger.info(f"[Domain]: {domain}")
        logger.info(f"[Example id]: {eid}")
        logger.info(f"[Result dir]: {result_dir}")
        logger.info(f"[Instruction]: {example['instruction']}")

        # example start running
        try:
            score = lib_run_single.run_single_example(agent, env, example, result_dir, args)
            scores[domain].append(score)
        except Exception as e: # do not record in this case
            logger.error(f"Exception in {domain}/{eid}: {e}")
            # env.controller.end_recording(os.path.join(result_dir, "recording.mp4"))
            with open(os.path.join(result_dir, "trajectory.jsonl"), "a") as f:
                f.write(json.dumps({
                    "Error": f"Error msg in {domain}/{eid}: {e}"
                }))
                f.write("\n")

        root_logger.removeHandler(example_handler)
        example_handler.close()

    env.close()
    return scores


def get_result_dir(args):
    """ Method to define the unique result directory for the current experiment. For example, the result directory is `results/pyautogui_a11y_tree_gpt-4o-2024-05-13`, and the example directory is `results/pyautogui_a11y_tree_gpt-4o-2024-05-13/dbt/4d2e1-34e134-rfqe32/` for example id `4d2e1-34e134-rfqe32` under tool `dbt`. And the following files will be saved:
    - `trajectory.jsonl`: trajectory information for each step
    - `result.txt`: evaluation result for the example, this is also an indicator of whether the example is finished (see func `get_examples`)
    - `log.txt`: log message when running the example
    - `recording.mp4`: recording video for the example
    - `screenshots/`: directory containing all screenshots for each step if observation space contains screenshot
        - `step_1_2021-01-01@12:00:00.png`
    - `a11y_trees/`: directory containing all a11y trees for each step if observation space contains a11y tree
        - `step_1_2021-01-01@12:00:00.txt`
    """
    result_dir = f"{args.action_space}_{args.observation_space}_{args.model}"
    if args.rag:
        result_dir += '_rag'
        if not args.rag_filename.endswith('txt'):
            suffix = os.path.splitext(args.rag_filename)[1]
            result_dir += suffix
    if args.execution_feedback:
        result_dir += '_ef'
    # result_dir += f"_temp{args.temperature}_traj{args.max_trajectory_length}"
    return os.path.join(args.result_dir, result_dir)


def get_examples(args, result_dir: str, easy_first: bool = True) -> List[Dict[str, str]]:
    """ Get [Filter] the list of example dict for the current experiment.
    # Filter method:
    - args.from_scratch (bool): if True, ignore existing results in result.txt, otherwise,
        only test examples that are unfinished under the result directory
    - args.domains (List[str]): if not contain "all", only include examples under the specified domains
    - args.exclude_account (bool): if True, exclude examples that are related to real accounts
    - easy_first (bool): if True, sort examples that are easy to run first (smaller action_number)

    # The returned dict for each example in the List containing:
        - id: example id
        - domain: example domain, a.k.a., professional tool name
        - config: .json config path for the example
        - result: path to the result directory for the example
            note that, the result directory will also be reset implicitly
    """
    def file_not_empty(fp):
        with open(fp, 'r') as f:
            content = f.read().strip()
            return len(content) > 0

    examples_to_run = []
    data_dir = os.path.join("evaluation_examples", "examples")
    filtered_domain = ALL_DOMAINS if 'all' in args.domains else args.domains
    test_data = json.load(open(args.example, 'r'))
    for domain in os.listdir(data_dir):
        if domain not in filtered_domain or domain not in test_data: continue
        domain_dir = os.path.join(data_dir, domain)
        domain_result_dir = os.path.join(result_dir, domain)
        os.makedirs(domain_result_dir, exist_ok=True)

        for example_id in test_data[domain]:
            example_dir = os.path.join(domain_dir, example_id)
            if not os.path.isdir(example_dir): continue

            example_result_dir = os.path.join(domain_result_dir, example_id)
            result_file = os.path.join(example_result_dir, "result.txt")
            if not args.from_scratch and os.path.exists(result_file) and file_not_empty(result_file): continue
            data_config = os.path.join(example_dir, f"{example_id}.json")
            data = json.load(open(data_config, 'r'))
            if args.exclude_account and 'account' in data['tags']: continue

            # remove the result directory if exists
            shutil.rmtree(example_result_dir, ignore_errors=True)
            os.makedirs(example_result_dir, exist_ok=True)
            if args.observation_space != "a11y_tree":
                os.makedirs(os.path.join(example_result_dir, "screenshots"), exist_ok=True)
            if args.observation_space != "screenshot":
                os.makedirs(os.path.join(example_result_dir, "a11y_trees"), exist_ok=True)
            example = {
                "id": example_id,
                "domain": domain,
                "config": data_config,
                "result": example_result_dir,
                "action_number": data["action_number"]
            }
            examples_to_run.append(example)

    logger.info(f"Total examples to run: {len(examples_to_run)}")
    if easy_first:
        sorted(examples_to_run, key=lambda x: x['action_number'])
    return examples_to_run


def get_result(result_dir: dict) -> str:
    """ Get existing results.
    """
    all_result = {}
    for domain in os.listdir(result_dir):
        domain_path = os.path.join(result_dir, domain)
        if not os.path.isdir(domain_path): continue
        if domain not in all_result:
            all_result[domain] = []
        for example_id in os.listdir(domain_path):
            example_path = os.path.join(domain_path, example_id)
            if not os.path.isdir(example_path): continue
            if "result.txt" in os.listdir(example_path):
                all_result[domain].append(float(open(os.path.join(example_path, "result.txt"), "r").read()))
    total = sum([len(all_result[domain]) for domain in all_result])
    if total == 0:
        return "New experiment, no result yet."
    else:
        total_success = sum([sum(all_result[domain]) for domain in all_result])
        msg = f"Current Success Rate: {total_success} / {total} = { total_success / total * 100:.2f}%"
        return msg


if __name__ == '__main__':
    os.environ["TOKENIZERS_PARALLELISM"] = "false"
    args = config()

    result_dir = get_result_dir(args)
    examples = get_examples(args, result_dir)

    logger.info(f"Old result before running:\n{get_result(result_dir)}")
    test(args, examples)
    logger.info(f"New result after running:\n{get_result(result_dir)}")
