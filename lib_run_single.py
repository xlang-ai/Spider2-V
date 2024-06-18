#coding=utf8
import datetime, json, logging, os, sys, argparse
from typing import List, Optional, Union, Dict, Tuple
from desktop_env.envs.desktop_env import DesktopEnv
from mm_agents.agent import PromptAgent
from wrapt_timeout_decorator import *

logger = logging.getLogger("desktopenv.experiment")

TIME_LIMIT = 1800 # 30 minutes for each example at most

@timeout(TIME_LIMIT, use_signals=False)
def run_single_example(agent: PromptAgent, env: DesktopEnv, example: dict, result_dir: str, args: argparse.Namespace) -> float:
    done, step_idx = False, 0
    agent.reset()
    obs = env.reset(task_config=example)
    infos = []
    env.controller.start_recording()
    screenshots = os.path.join(result_dir, "screenshots")
    a11y_tree = os.path.join(result_dir, "a11y_trees")

    while not done and step_idx < args.max_steps:
        context = example['context'] if 'context' in example else None
        response, actions = agent.predict(example['instruction'], obs, context)
        infos = []
        for action in actions:
            # Capture the timestamp before executing the action
            action_timestamp = datetime.datetime.now().strftime("%Y%m%d@%H%M%S")
            logger.info("[Action]: Step %d: %s", step_idx + 1, action)

            obs, reward, done, info = env.step(action, args.sleep_after_execution)
            infos.append(info) # add action execution result to the observation

            # Save screenshot and trajectory information
            if args.observation_space != 'a11y_tree':
                with open(os.path.join(screenshots, f"step_{step_idx + 1}_{action_timestamp}.png"), "wb") as _f:
                    _f.write(agent.observations[-1]["raw_screenshot"])
            if args.observation_space != 'screenshot':
                with open(os.path.join(a11y_tree, f"step_{step_idx + 1}_{action_timestamp}.txt"), "w", encoding='utf-8') as _f:
                    _f.write(agent.observations[-1]["accessibility_tree"])
            # write trajectory information (can replay the trajectory later)
            with open(os.path.join(result_dir, "trajectory.jsonl"), "a") as f:
                f.write(json.dumps({
                    "step_num": step_idx + 1,
                    "action_timestamp": action_timestamp,
                    "action": action,
                    "reward": reward,
                    "done": done,
                    "info": info
                }) + '\n')
            if done:
                logger.info("[INFO]: The episode is done. Congratulations!")
                break
        if done: break
        obs['infos'] = infos
        step_idx += 1
    else:
        logger.warning("[WARNING]: Exceeded the maximum number of steps. Forced to stop the episode.")

    agent.get_current_cost()
    try: # for safety reason, wrap the evaluation in a try-except block
        result = env.evaluate()
    except Exception as e:
        error_msg = f"[ERROR]: Unexpected error occurred when evaluating the result: {e}"
        logger.error(error_msg)
        result = 0.0

    logger.info(f"[Result]: Evaluation score for {example['id']}: {result:.1f}")
    with open(os.path.join(result_dir, "result.txt"), "w", encoding="utf-8") as f:
        f.write(f"{result}\n")

    env.controller.end_recording(os.path.join(result_dir, "recording.mp4"))
    return result