#coding=utf8
import json, argparse, random
import logging, os, sys, datetime
from typing import Dict, Any, List, Optional
from desktop_env.envs.desktop_env import DesktopEnv


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
os.makedirs("logs", exist_ok=True)
datetime_str: str = datetime.datetime.now().strftime("%Y%m%d@%H%M%S")
file_handler = logging.FileHandler(os.path.join("logs", "normal-{:}.log".format(datetime_str)))
debug_handler = logging.FileHandler(os.path.join("logs", "debug-{:}.log".format(datetime_str)))
stdout_handler = logging.StreamHandler(sys.stdout)
file_handler.setLevel(logging.INFO)
debug_handler.setLevel(logging.DEBUG)
stdout_handler.setLevel(logging.INFO)
formatter = logging.Formatter(fmt="\x1b[1;33m[%(asctime)s \x1b[31m%(levelname)s \x1b[32m%(module)s/%(lineno)d-%(processName)s\x1b[1;33m] \x1b[0m%(message)s")
file_handler.setFormatter(formatter)
debug_handler.setFormatter(formatter)
stdout_handler.setFormatter(formatter)
stdout_handler.addFilter(logging.Filter("desktopenv"))
logger.addHandler(file_handler)
logger.addHandler(debug_handler)
logger.addHandler(stdout_handler)
logger = logging.getLogger("desktopenv.human")


def run_human_agent():
    """ Usage:
    python run_spider2v_human.py -p /path/to/vm.vmx -s {snapshot_name} -e evaluation_examples/test_non_account.json
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path_to_vm', type=str, help="path to the virtual machine .vmx file.")
    parser.add_argument('-s', '--snapshot', type=str, default="init_state", help="snapshot name")
    parser.add_argument('-e', '--example', type=str, help='.json file path to examples')
    parser.add_argument('-r', '--recording', default='recordings', help='folder to save trajectory videos')
    args = parser.parse_args()
    os.makedirs(args.recording, exist_ok=True)

    if not args.example:
        args.example = os.path.join('evaluation_examples', 'test_one.json')
        logger.warning(f'[WARNING]: No example provided. Will use {args.example} by default.')
    with open(args.example, 'r') as infile:
        examples = json.load(infile)
    checking_list = [os.path.join('evaluation_examples', 'examples', tool, uid, f'{uid}.json') for tool in examples for uid in examples[tool]]

    env = DesktopEnv(
        path_to_vm=args.path_to_vm,
        snapshot_name=args.snapshot,
        action_space="computer_13"
    )
    try:
        for example_path in checking_list:
            with open(example_path, 'r', encoding='utf-8', errors='ignore') as inf:
                example = json.load(inf)

            # reset the environment
            env.reset(task_config=example)
            logger.info(f'\x1b[32m[Task instruction for {example["snapshot"]}/{example["id"]}]:\x1b \n{example["instruction"]}\x1b[0m')
            
            # recoding the human trajectory
            recording_path = os.path.join(args.recording, example["id"])
            os.makedirs(recording_path, exist_ok=True)
            recording_file = os.path.join(recording_path, "recording.mp4")

            # load the oracle action prompt
            verbose_instruction = os.path.join(os.path.dirname(example_path), 'verbose_instruction.txt')
            if os.path.exists(verbose_instruction):
                with open(verbose_instruction, 'r', encoding='utf-8', errors='ignore') as inf:
                    verbose_instruction = inf.read().strip()
            else: verbose_instruction = None

            while True:
                action = input("\033[31m[Action] Please enter your action number, chosen from:\n1. start recording;\n2. end recording (by default, the original video will be overwritten);\n3. evaluate;\n4. end recording and evaluate (indeed 2+3);\n5. reset VM environment;\n6. show verbose instruction for reference;\n7. switch to the next example.\nYour choice is (Press Ctrl+C to exit): \033[0m")

                if action.strip() in ['1', 'start']: # start recoding and timing
                    env.controller.start_recording()
                elif action.strip() in ['2', 'end']: # end recording and evaluate the result
                    env.controller.end_recording(recording_file)
                    logger.info(f'Recording saved to {recording_file}')
                elif action.strip() in ['3', 'evaluate']:
                    score = env.evaluate()
                    logger.info(f"Evaluation score: {score}")
                elif action.strip() in ['4']:
                    env.controller.end_recording(recording_file)
                    logger.info(f'Recording saved to {recording_file}')
                    score = env.evaluate()
                    logger.info(f"Evaluation score: {score}")
                elif action.strip() in ['5', 'reset']: # reset the environment
                    env.reset(task_config=example)
                    logger.info(f'\x1b[32m[Task instruction for example {example["snapshot"]}/{example["id"]}]:\x1b \n{example["instruction"]}\x1b[0m')
                elif action.strip() in ['6', 'verbose']:
                    logger.info(f'Verbose instruciton is: {verbose_instruction if verbose_instruction else "Not found."}')
                elif action.strip() in ['7', 'next']:
                    logger.info('Switching to the next example ...')
                    break
                else:
                    logger.error('Unrecognized action. Please try again...')

    except KeyboardInterrupt:
        logger.info('Keyboard interruption detected. Exiting...')
    except Exception as e:
        logger.error(f'[ERROR]: Unexpected error occurred. {e}')

    env.close()
    logger.info('Environment closed.')
    return


if __name__ == "__main__":

    run_human_agent()
