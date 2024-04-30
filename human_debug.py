import json, argparse
from desktop_env.envs.desktop_env import DesktopEnv
from desktop_env.envs.actions import KEYBOARD_KEYS
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

logger = logging.getLogger("desktopenv.human_debug")

instruction = """
Debugging one example, you can directly work in VM or type in:
1. reset/RESET: reset the environment to the initial state.
2. evaluate/EVALUATE: evaluate the current state of the environment.
3. exit/EXIT: exit the environment and program.
4. concrete action dict in desktop_env/envs/actions.py, e.g., '{"action_type": "TYPING", "parameters": {"text": "echo hello"}}'
(note that, the string of action dict should use double quotes for string keys and values)
Now, let us start:
"""

def human_agent():
    """ Runs the Gym environment with human input.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', type=str, default="/Users/happysix/Virtual Machines.localized/Ubuntu-22.04.vmwarevm/Ubuntu-22.04.vmx", help="Path to the virtual machine .vmx file.")
    parser.add_argument('-s', '--snapshot', type=str, help="Snapshot to load.", required=True)
    parser.add_argument('-e', '--example', type=str, required=True)
    args = parser.parse_args(sys.argv[1:])
    with open(args.example, "r") as f:
        example = json.load(f)
    if args.snapshot: example['snapshot'] = args.snapshot
    env = DesktopEnv(
        path_to_vm=args.path,
        snapshot_name=example['snapshot'],
        action_space="computer_13"
    )

    # reset the environment to certain snapshot (add proxy if needed)
    # observation = env.reset(task_config=example, proxy={'host': "172.16.12.1", "port": 58591})
    observation = env.reset(task_config=example)
    done = False

    logger.info(instruction)

    while True:
        try:
            action_str = input("Please input action (enter EXIT or Ctrl+C to exit): ")
            if action_str.strip().lower() == 'exit':
                logger.info('Exiting ENV...')
                break
            if action_str.strip().lower() == 'reset':
                env.reset(task_config=example)
                logger.info('Reset the environment ...')
                continue
            if action_str.strip().lower() == 'evaluate':
                result = env.evaluate()
                logger.info("Result: %.2f", result)
                continue
            
            try:
                action = json.loads(action_str)
                logger.info("Take Action: %s", json.dumps(action, ensure_ascii=False))
            except:
                logger.error(f'[ERROR]: Failed to parser action string, please check the format: {action_str}')
                continue

            observation, reward, done, info = env.step(action, pause=1)

            logger.info("Observation[screenshot]: %s" % (observation['screenshot']))
            logger.info("================================\n")
            if done:
                logger.info("Episode finished.")
                break
        except KeyboardInterrupt:
            logger.info('Keyboard interruption detected. Exiting...')
            break
        except Exception as e:
            logger.exception("Unknown exception occurred. Exiting...")
            break

    # env.close()
    # logger.info("Environment closed.")


if __name__ == "__main__":

    human_agent()
