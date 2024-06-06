#coding=utf8
import json, argparse
from desktop_env.envs.desktop_env import DesktopEnv
from typing import Dict, Any, List, Optional
import logging
import os
import sys
import datetime

#  Logger Configs {{{ # 
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

datetime_str: str = datetime.datetime.now().strftime("%Y%m%d@%H%M%S")

file_handler = logging.FileHandler(os.path.join("logs", "normal-{:}.log".format(datetime_str)))
debug_handler = logging.FileHandler(os.path.join("logs", "debug-{:}.log".format(datetime_str)))
stdout_handler = logging.StreamHandler(sys.stdout)
sdebug_handler = logging.FileHandler(os.path.join("logs", "sdebug-{:}.log".format(datetime_str)))

file_handler.setLevel(logging.INFO)
debug_handler.setLevel(logging.DEBUG)
stdout_handler.setLevel(logging.INFO)
sdebug_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter(fmt="\x1b[1;33m[%(asctime)s \x1b[31m%(levelname)s \x1b[32m%(module)s/%(lineno)d-%(processName)s\x1b[1;33m] \x1b[0m%(message)s")
file_handler.setFormatter(formatter)
debug_handler.setFormatter(formatter)
stdout_handler.setFormatter(formatter)
sdebug_handler.setFormatter(formatter)

stdout_handler.addFilter(logging.Filter("desktopenv"))
sdebug_handler.addFilter(logging.Filter("desktopenv"))

logger.addHandler(file_handler)
logger.addHandler(debug_handler)
logger.addHandler(stdout_handler)
logger.addHandler(sdebug_handler)
#  }}} Logger Configs # 

logger = logging.getLogger("desktopenv.human_validation")


def validate_example(example: str) -> str:
    """ Given an example uuid or sub-path, return a valid example path, e.g., evaluation_examples/examples/{tool_name}/uuid/uuid.json
    """
    folders = example.strip().split(os.path.sep)
    if not folders[-1].endswith('.json'):
        folders.append(folders[-1] + '.json')
    if len(folders) > 5: raise ValueError(f"Invalid example path: {example}")
    if len(folders) == 5:
        return os.path.join(*folders)
    if len(folders) >= 3:
        return os.path.join('evaluation_examples', 'examples', folders[-3], folders[-2], folders[-1])
    
    ex_id = folders[-1][:-5]
    # search for the tool name
    for tool_name in os.listdir(os.path.join('evaluation_examples', 'examples')):
        if tool_name == 'libreoffice_calc': continue
        subdir = os.path.join('evaluation_examples', 'examples', tool_name)
        if not os.path.isdir(subdir): continue
        files = os.listdir(subdir)
        if ex_id in files:
            return os.path.join(subdir, ex_id, ex_id + '.json')
    raise ValueError(f"Invalid example path: {example}")


def human_agent():
    """ Runs the Gym environment with human input. Usage:
    1. python human_validation.py -p /path/to/vm.vmx -s {snapshot_name} -e evaluation_examples/examples/{tool_name}/{uuid}/{uuid}.json
    2. python human_validation.py -p /path/to/vm.vmx -s {snapshot_name} --example_from_file file.txt, where file.txt contains a list of example uuids, one per line, e.g.,
        8a8b875d-1f10-40fa-b998-8fd8ebb3515b
        8a8b875d-1f10-40fa-b998-8fd8ebb3515b
        ...
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', type=str, help="Path to the virtual machine .vmx file.")
    parser.add_argument('-s', '--snapshot', type=str, required=True, help="Snapshot to load.")
    parser.add_argument('-e', '--example', type=str, help='.json file path to a specific example to validate')
    parser.add_argument('--example_from_file', type=str, help='Path to the file, each line containing an example id to validate.')
    parser.add_argument('-r', '--recording', type=str, default='recordings', help='recording directory')
    parser.add_argument('--proxy', action='store_true', help='Use network proxy for VMWare network')
    parser.add_argument('--host', type=str, default='172.16.12.1', help='Network proxy host ip address')
    parser.add_argument('--port', type=int, default=58591, help='Network proxy port')
    args = parser.parse_args(sys.argv[1:])
    os.makedirs(args.recording, exist_ok=True)

    if args.example:
        checking_list = [validate_example(args.example)]
    else:
        assert args.example_from_file, "Either --example or --example_from_file should be provided."
        with open(args.example_from_file, 'r', encoding='utf-8', errors='ignore') as inf:
            checking_list = [validate_example(line.strip()) for line in inf if line.strip() != '']

    env = DesktopEnv(
        path_to_vm=args.path,
        snapshot_name=args.snapshot,
        action_space="computer_13"
    )
    try:
        for example_path in checking_list:
            with open(example_path, 'r', encoding='utf-8', errors='ignore') as inf:
                example = json.load(inf)

            # reset the environment to certain snapshot (add proxy if needed)
            if args.proxy:
                env.reset(task_config=example, proxy={'host': args.host, "port": args.port})
            else:
                env.reset(task_config=example)
            logger.info(f'\x1b[32m[Task instruction for example {example["id"]}]:\x1b \n{example["instruction"]}\x1b[0m')
            
            # recoding the human trajectory
            recording_path = os.path.join(args.recording, example["id"])
            os.makedirs(recording_path, exist_ok=True)
            recording_file = os.path.join(recording_path, "recording.mp4")

            verbose_instruction = os.path.join(os.path.dirname(example_path), 'verbose_instruction.txt')
            if os.path.exists(verbose_instruction):
                with open(verbose_instruction, 'r', encoding='utf-8', errors='ignore') as inf:
                    verbose_instruction = inf.read().strip()
            else: verbose_instruction = None

            while True:
                action = input("\033[31m[Action] Please enter your action number, chosen from:\n1. start recording;\n2. end recording (by default, the original video will be overwritten);\n3. evaluate;\n4. end recording and evaluate (indeed 2+3);\n5. reset VM environment;\n6. show verbose instruction for reference;\n7. switch to the next example.\n8. Take a screenshot and save to local file.\nYour choice is (Press Ctrl+C to exit): \033[0m")

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
                    if args.proxy:
                        env.reset(task_config=example, proxy={'host': args.host, "port": args.port})
                    else:
                        env.reset(task_config=example)
                    logger.info(f'\x1b[32m[Task instruction for example {example["id"]}]:\x1b \n{example["instruction"]}\x1b[0m')
                elif action.strip() in ['6', 'verbose']:
                    logger.info(f'Verbose instruciton is: {verbose_instruction if verbose_instruction else "Not found."}')
                elif action.strip() == '8':
                    image = env.controller.get_screenshot()
                    with open('screenshot.png', 'wb') as file:
                        file.write(image)
                    logger.info("screenshot downloaded to screenshot.png ...")
                elif action.strip() in ['7', 'next']:
                    logger.info('Switching to the next example ...')
                    break
                else:
                    logger.error('Unrecognized action. Please try again...')

    except KeyboardInterrupt:
        logger.info('Keyboard interruption detected. Exiting...')
        exit(0)
    # except Exception as e:
    #     logger.error(f'[ERROR]: Unexpected error occurred. {e}')
    #     exit(1)

    # env.close()
    logger.info(f"Validation for {len(checking_list)} examples completed.")


if __name__ == "__main__":

    human_agent()
