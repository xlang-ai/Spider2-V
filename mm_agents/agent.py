import base64
import json
import logging
import os
import re
import tempfile
import time
import xml.etree.ElementTree as ET
from http import HTTPStatus
from io import BytesIO
from typing import Dict, List, Tuple, Union

import backoff
import dashscope
import google.generativeai as genai
import openai
from groq import Groq

import requests
import tiktoken
from PIL import Image
from google.api_core.exceptions import InvalidArgument, ResourceExhausted, InternalServerError, BadRequest

from mm_agents.accessibility_tree_wrap.heuristic_retrieve import filter_nodes, draw_bounding_boxes
from mm_agents.prompt_templates import ACTION_SPACE_PROMPTS, OBSERVATION_SPACE_PROMPTS, SYSTEM_PROMPT

logger = logging.getLogger("desktopenv.agent")

pure_text_settings = ['a11y_tree']


# Function to encode the image
def encode_image(image_content):
    return base64.b64encode(image_content).decode('utf-8')


def encoded_img_to_pil_img(data_str):
    base64_str = data_str.replace("data:image/png;base64,", "")
    image_data = base64.b64decode(base64_str)
    image = Image.open(BytesIO(image_data))

    return image


def save_to_tmp_img_file(data_str):
    base64_str = data_str.replace("data:image/png;base64,", "")
    image_data = base64.b64decode(base64_str)
    image = Image.open(BytesIO(image_data))

    tmp_img_path = os.path.join(tempfile.mkdtemp(), "tmp_img.png")
    image.save(tmp_img_path)

    return tmp_img_path


def get_model_pricing(model_name: str) -> Tuple[float, float]:
    pricing = {
        'gpt-3.5-turbo': {
            'prompt': 0.5e-6,
            'completion': 1.5e-6
        },
        'gpt-4-turbo': {
            'prompt': 10e-6,
            'completion': 30e-6
        },
        'gpt-4o': {
            'prompt': 5e-6,
            'completion': 15e-6
        }
    }
    if model_name.startswith('gpt-3.5'): model_name = 'gpt-3.5-turbo'
    elif model_name.startswith('gpt-4o'): model_name = 'gpt-4o'
    elif model_name.startswith('gpt-4'): model_name = 'gpt-4-turbo'
    if model_name in pricing:
        return pricing[model_name]['prompt'], pricing[model_name]['completion']
    logger.warning(f"Model {model_name} is not in the pricing list.")
    return 0.0, 0.0


def linearize_accessibility_tree(filtered_nodes: List[ET.Element], add_index: bool = False) -> str:
    # leaf_nodes = find_leaf_nodes(accessibility_tree)
    # first line is headers
    if add_index:
        linearized_accessibility_tree = ["INDEX\tTAG\tNAME\tPOSITION (top-left x & y)\tSIZE (width & height)\tTEXT"]
    else:
        linearized_accessibility_tree = ["TAG\tNAME\tPOSITION (top-left x & y)\tSIZE (width & height)\tTEXT"]
    # Linearize the accessibility tree nodes into a table format
    for idx, node in enumerate(filtered_nodes):
        # linearized_accessibility_tree += node.tag + "\t"
        # linearized_accessibility_tree += node.attrib.get('name') + "\t"
        if node.text:
            text = node.text.strip()
            # text = (node.text if '"' not in node.text \
                        # else '"{:}"'.format(node.text.replace('"', '""'))
                    # )
        elif node.get("{uri:deskat:uia.windows.microsoft.org}class", "").endswith("EditWrapper") \
                and node.get("{uri:deskat:value.at-spi.gnome.org}value"):
            text: str = node.get("{uri:deskat:value.at-spi.gnome.org}value").strip()
            # text = (text if '"' not in text \
                        # else '"{:}"'.format(text.replace('"', '""'))
                    # )
        else:
            text = ""
        text = "{:}".format(repr(text))
        # linearized_accessibility_tree += node.attrib.get(
        # , "") + "\t"
        # linearized_accessibility_tree += node.attrib.get('{uri:deskat:component.at-spi.gnome.org}size', "") + "\n"
        entry = f"{idx + 1}\t" if add_index else "" # index starting from 1, see draw_bounding_boxes()
        entry += "{:}\t{:}\t{:}\t{:}\t{:}".format(
                node.tag, node.get("name", "")
                , node.get('{uri:deskat:component.at-spi.gnome.org}screencoord', "")
                , node.get('{uri:deskat:component.at-spi.gnome.org}size', "")
                , text
            )
        linearized_accessibility_tree.append(entry)

    return "\n".join(linearized_accessibility_tree)


def parse_actions_from_string(input_string):
    if input_string.strip() in ['WAIT', 'DONE', 'FAIL']:
        return [input_string.strip()]
    # Search for a JSON string within the input string
    actions = []
    matches = re.findall(r'```json\s+(.*?)\s+```', input_string, re.DOTALL)
    if matches:
        # Assuming there's only one match, parse the JSON string into a dictionary
        try:
            for match in matches:
                action_dict = json.loads(match)
                actions.append(action_dict)
            return actions
        except json.JSONDecodeError as e:
            return f"Failed to parse JSON: {e}"
    else:
        matches = re.findall(r'```\s+(.*?)\s+```', input_string, re.DOTALL)
        if matches:
            # Assuming there's only one match, parse the JSON string into a dictionary
            try:
                for match in matches:
                    action_dict = json.loads(match)
                    actions.append(action_dict)
                return actions
            except json.JSONDecodeError as e:
                return f"Failed to parse JSON: {e}"
        else:
            try:
                action_dict = json.loads(input_string)
                return [action_dict]
            except json.JSONDecodeError:
                raise ValueError("Invalid response format: " + input_string)


def parse_code_from_string(input_string):
    input_string = "\n".join([line.strip() for line in input_string.split(';') if line.strip()])
    if input_string.strip() in ['WAIT', 'DONE', 'FAIL']:
        return [input_string.strip()]

    # This regular expression will match both ```code``` and ```python code```
    # and capture the `code` part. It uses a non-greedy match for the content inside.
    pattern = r"```(?:\w+\s+)?(.*?)```"
    # Find all non-overlapping matches in the string
    matches = re.findall(pattern, input_string, re.DOTALL)

    # The regex above captures the content inside the triple backticks.
    # The `re.DOTALL` flag allows the dot `.` to match newline characters as well,
    # so the code inside backticks can span multiple lines.

    # matches now contains all the captured code snippets

    codes = []

    for match in matches:
        match = match.strip()
        commands = ['WAIT', 'DONE', 'FAIL']  # fixme: updates this part when we have more commands

        if match in commands:
            codes.append(match.strip())
        elif match.split('\n')[-1] in commands:
            if len(match.split('\n')) > 1:
                codes.append("\n".join(match.split('\n')[:-1]))
            codes.append(match.split('\n')[-1])
        else:
            codes.append(match)

    return codes


def parse_code_from_som_string(input_string, masks):
    # parse the output string by masks
    tag_vars = ""
    indexes = re.findall(r"index_(\d+)", input_string)
    for index in indexes:
        try:
            x = int(index) - 1
            if 0 <= x < len(masks):
                x, y, w, h = masks[x]
                tag_vars += "index_" + index + " = ({}, {})".format(int(x + w // 2), int(y + h // 2))
                tag_vars += "\n"
        except: pass

    actions = parse_code_from_string(input_string)

    for i, action in enumerate(actions):
        if action.strip() in ['WAIT', 'DONE', 'FAIL']:
            pass
        else:
            action = tag_vars + action
            actions[i] = action

    return actions


def trim_accessibility_tree(linearized_accessibility_tree, max_tokens):
    enc = tiktoken.encoding_for_model("gpt-4")
    tokens = enc.encode(linearized_accessibility_tree)
    if len(tokens) > max_tokens:
        linearized_accessibility_tree = enc.decode(tokens[:max_tokens])
        linearized_accessibility_tree += "[...]\n"
    return linearized_accessibility_tree


class PromptAgent:
    def __init__(
            self,
            platform="ubuntu",
            model="gpt-4o",
            max_tokens=1500,
            top_p=0.9,
            temperature=0.5,
            action_space="computer_13",
            observation_space="screenshot_a11y_tree",
            # observation_space can be in ["screenshot", "a11y_tree", "screenshot_a11y_tree", "som"]
            execution_feedback=True,
            screen_size={'width': 1920, "height": 1080},
            max_trajectory_length=3,
            a11y_tree_max_tokens=5000
    ):
        self.platform = platform
        self.model = model
        self.max_tokens = max_tokens
        self.top_p = top_p
        self.temperature = temperature
        self.action_space = action_space
        self.observation_space = observation_space
        self.max_trajectory_length = max_trajectory_length
        self.a11y_tree_max_tokens = a11y_tree_max_tokens

        self.thoughts = []
        self.actions = []
        self.observations = []
        self.execution_feedback = execution_feedback
        self.usages = {"prompt_tokens": 0, "completion_tokens": 0}

        action_key = self.action_space if 'som' not in self.observation_space else self.action_space + '_som'
        action_prompt = ACTION_SPACE_PROMPTS[action_key]
        observation_prompt = OBSERVATION_SPACE_PROMPTS[self.observation_space]
        self.system_message = SYSTEM_PROMPT.format(action_prompt=action_prompt, observation_prompt=observation_prompt, screen_width=screen_size['width'], screen_height=screen_size['height'])


    def get_current_cost(self) -> str:
        pc, cc = get_model_pricing(self.model)
        total_cost = pc * self.usages["prompt_tokens"] + cc * self.usages["completion_tokens"]
        logger.info(f'[INFO]: Current usage: {self.usages["prompt_tokens"] * 1e-6:.2f}M prompt tokens, {self.usages["completion_tokens"] * 1e-6:.2f}M completion tokens, cost ${total_cost:.2f} .')
        return


    def add_action_infos(self, messages, action_list: List[Union[str, Dict]], infos: List[Dict], failed_only: bool = True) -> Dict:
        """ Add parsed actions (`action_list`) and action execution flags (`infos`) to the messages.
        @args:
            failed_only(bool): only add actions which are failed to the messages
        @return:
            messages: updated messages list
        """
        if not infos: return messages
        if failed_only: # only add failed actions and flags into messages
            for info in infos:
                if info['status'] == 'error' or info['error'].strip() != "":
                    break
            else: return messages

        prefix_msg = 'Here are the parsed action list from your last response and the execution flag of each action from the desktop environment:\n' if not failed_only else 'Here are the failed actions and their execution feedbacks of your last response:\n'
        content_msg = ''
        assert len(action_list) == len(infos), "The number of actions and infos should be the same."

        def _execution_msg(info):
            if info['status'] == 'error':
                return f"Failed with error message -> {info['message'].strip()}"
            elif info['error'].strip() != "":
                return f"Succeed with error message -> {info['error'].strip()}"
            else:
                return "Succeed without error."

        if len(action_list) == 0:
            for action, info in zip(action_list, infos):
                if failed_only and (info['status'] == 'success' and info['error'].strip() == ""):
                    continue # action executed successfully, just skip
                if self.action_space == 'computer_13':
                    content_msg += f"\nParsed action: {json.dumps(action, ensure_ascii=False)}\n"
                    content_msg += f"Execution flag: {_execution_msg(info)}\n"
                elif self.action_space == 'pyautogui':
                    content_msg += f"\nParsed action:\n```\n{action}\n```\n"
                    content_msg += f"Execution flag: {_execution_msg(info)}\n"
                else:
                    raise ValueError("Unrecognised action_space type: " + self.action_space)
        else:
            content_msg = "\nNo valid action detected from your previous response.\n"
        suffix_msg = '\nIf there are any omissions or additions of actions, please meticulously check the specification of the action space; if the execution status of any action is incorrect or unexpected, try to resolve it based on the latest observations below.' if not failed_only else 'Please meticulously check the error messages and the execution status of the failed actions, and try to resolve them based on the latest observations below.'
        msg = {"role": "user", "content": [{"type": "text", "text": prefix_msg + content_msg + suffix_msg}]}
        messages.append(msg)
        return messages


    def predict(self, instruction: str, obs: Dict, context: str = None) -> List:
        """
        Predict the next action(s) based on the current observation.
        """
        system_message = self.system_message + "\nYou are asked to complete the following task: {}".format(instruction)

        # Prepare the payload for the API call
        messages = []
        masks = None

        messages.append({
            "role": "system",
            "content": [
                {
                    "type": "text",
                    "text": system_message
                },
            ]
        })

        if context is not None:
            context_message = "We also retrieve relevant documentation from the web to help you with the task:\n{}".format(context)
            messages.append({
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        "text": context_message
                    },
                ]
            })

        # Append trajectory
        assert len(self.observations) == len(self.actions) and len(self.actions) == len(self.thoughts) \
            , "The number of observations and actions should be the same."

        if len(self.observations) > self.max_trajectory_length:
            if self.max_trajectory_length == 0:
                _observations = []
                _actions = []
                _thoughts = []
            else:
                _observations = self.observations[-self.max_trajectory_length:]
                _actions = self.actions[-self.max_trajectory_length:]
                _thoughts = self.thoughts[-self.max_trajectory_length:]
        else:
            _observations = self.observations
            _actions = self.actions
            _thoughts = self.thoughts

        for previous_obs, previous_action, previous_thought in zip(_observations, _actions, _thoughts):

            # {{{1
            if self.observation_space == "screenshot_a11y_tree":
                _screenshot = previous_obs["screenshot"]
                _linearized_accessibility_tree = previous_obs["accessibility_tree"]

                messages.append({
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "Given the text of accessibility tree and image of screenshot as below:\n{}\nWhat's the next step that you will do to help with the task?".format(_linearized_accessibility_tree)
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/png;base64,{_screenshot}",
                                "detail": "high"
                            }
                        }
                    ]
                })
            elif self.observation_space in ["som"]:
                _screenshot = previous_obs["screenshot"]
                _linearized_accessibility_tree = previous_obs["accessibility_tree"]
                messages.append({
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "Given the text of accessibility tree and image of screenshot with index labels as below:\n{}\nWhat's the next step that you will do to help with the task?".format(_linearized_accessibility_tree)
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/png;base64,{_screenshot}",
                                "detail": "high"
                            }
                        }
                    ]
                })
            elif self.observation_space == "screenshot":
                _screenshot = previous_obs["screenshot"]

                messages.append({
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "Given the image of screenshot as below, what's the next step that you will do to help with the task?"
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/png;base64,{_screenshot}",
                                "detail": "high"
                            }
                        }
                    ]
                })
            elif self.observation_space == "a11y_tree":
                _linearized_accessibility_tree = previous_obs["accessibility_tree"]

                messages.append({
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "Given the text of accessibility tree as below:\n{}\nWhat's the next step that you will do to help with the task?".format(_linearized_accessibility_tree)
                        }
                    ]
                })
            else:
                raise ValueError("Invalid observation_space type: " + self.observation_space)  # 1}}}

            messages.append({
                "role": "assistant",
                "content": [
                    {
                        "type": "text",
                        "text": previous_thought.strip() if len(previous_thought) > 0 else "No valid action"
                    },
                ]
            })

        # action execution result of previous turn
        if len(self.actions) > 0 and self.execution_feedback: # if has previous action list
            infos = obs.get('infos', [])
            self.add_action_infos(messages, self.actions[-1], infos)

        # tackle the current observation
        if self.observation_space in ["screenshot", "screenshot_a11y_tree"]:
            base64_image = encode_image(obs["screenshot"])

            if self.observation_space == "screenshot_a11y_tree":
                filtered_nodes = filter_nodes(ET.fromstring(obs["accessibility_tree"]), self.platform, check_image=True)
                linearized_accessibility_tree = linearize_accessibility_tree(filtered_nodes, add_index=False)
                if linearized_accessibility_tree:
                    linearized_accessibility_tree = trim_accessibility_tree(linearized_accessibility_tree,
                                                                        self.a11y_tree_max_tokens)
                logger.debug("LINEAR AT: %s", linearized_accessibility_tree)

                self.observations.append({
                    "screenshot": base64_image,
                    "raw_screenshot": obs["screenshot"],
                    "accessibility_tree": linearized_accessibility_tree
                })
            else:
                self.observations.append({
                    "screenshot": base64_image,
                    "raw_screenshot": obs["screenshot"],
                    "accessibility_tree": None
                })

            messages.append({
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Given the image of screenshot as below, what's the next step that you will do to help with the task?"
                        if self.observation_space == "screenshot"
                        else "Given the text of accessibility tree and image of screenshot as below:\n{}\nWhat's the next step that you will do to help with the task?".format(linearized_accessibility_tree)
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{base64_image}",
                            "detail": "high"
                        }
                    }
                ]
            })
        elif self.observation_space == "a11y_tree":
            filtered_nodes = filter_nodes(ET.fromstring(obs["accessibility_tree"]), self.platform, check_image=True)
            linearized_accessibility_tree = linearize_accessibility_tree(filtered_nodes, add_index=False)

            if linearized_accessibility_tree:
                linearized_accessibility_tree = trim_accessibility_tree(linearized_accessibility_tree, self.a11y_tree_max_tokens)
            logger.debug("LINEAR AT: %s", linearized_accessibility_tree)

            self.observations.append({
                "screenshot": None,
                "accessibility_tree": linearized_accessibility_tree
            })

            messages.append({
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Given the text of accessibility tree as below:\n{}\nWhat's the next step that you will do to help with the task?".format(linearized_accessibility_tree)
                    }
                ]
            })
        elif self.observation_space == "som":
            # Add som to the screenshot
            filtered_nodes = filter_nodes(ET.fromstring(obs["accessibility_tree"]), self.platform, check_image=True)
            masks, drawn_nodes, tagged_screenshot = draw_bounding_boxes(filtered_nodes, obs['screenshot'])
            base64_image = encode_image(tagged_screenshot)
            linearized_accessibility_tree = linearize_accessibility_tree(drawn_nodes, add_index=True)
            if linearized_accessibility_tree:
                linearized_accessibility_tree = trim_accessibility_tree(linearized_accessibility_tree, self.a11y_tree_max_tokens)
            logger.debug("LINEAR AT: %s", linearized_accessibility_tree)

            self.observations.append({
                "screenshot": base64_image,
                "raw_screenshot": tagged_screenshot,
                "accessibility_tree": linearized_accessibility_tree
            })

            messages.append({
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Given the text of accessibility tree and image of screenshot with index labels as below:\n{}\nWhat's the next step that you will do to help with the task?".format(linearized_accessibility_tree)
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{base64_image}",
                            "detail": "high"
                        }
                    }
                ]
            })
        else:
            raise ValueError("Invalid observation_space type: " + self.observation_space)  # 1}}}

        # with open("messages.json", "w") as f:
        #     f.write(json.dumps(messages, indent=4))

        # logger.info("PROMPT: %s", messages)
        try:
            response = self.call_llm({
                "model": self.model,
                "messages": messages,
                "max_tokens": self.max_tokens,
                "top_p": self.top_p,
                "temperature": self.temperature
            })
        except Exception as e:
            logger.error("Failed to call" + self.model + ", Error: " + str(e))
            response = ""

        logger.info("RESPONSE: %s", response)

        try:
            actions = self.parse_actions(response, masks)
            self.thoughts.append(response)
        except ValueError as e:
            logger.error(f"[ERROR]: Failed to parse action from response {response}\nERROR_MSG: {e}")
            actions = []
            self.thoughts.append("")

        return response, actions

    @backoff.on_exception(
        backoff.constant,
        # here you should add more model exceptions as you want,
        # but you are forbidden to add "Exception", that is, a common type of exception
        # because we want to catch this kind of Exception in the outside to ensure each example won't exceed the time limit
        (
                # OpenAI exceptions
                openai.RateLimitError,
                openai.BadRequestError,
                openai.InternalServerError,

                # Google exceptions
                InvalidArgument,
                ResourceExhausted,
                InternalServerError,
                BadRequest,

                # Groq exceptions
                # todo: check
        ),
        interval=30,
        max_tries=10
    )
    def call_llm(self, payload):

        if self.model.startswith("gpt"):
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {os.environ['OPENAI_API_KEY']}"
            }
            logger.info("Generating content with GPT model: %s", self.model)
            response = requests.post(
                "https://api.openai.com/v1/chat/completions",
                headers=headers,
                json=payload
            )

            if response.status_code != 200:
                if response.json()['error']['code'] == "context_length_exceeded":
                    logger.error("Context length exceeded. Retrying with a smaller context.")
                    payload["messages"] = [payload["messages"][0]] + payload["messages"][-1:]
                    retry_response = requests.post(
                        "https://api.openai.com/v1/chat/completions",
                        headers=headers,
                        json=payload
                    )
                    if retry_response.status_code != 200:
                        logger.error(
                            "Failed to call LLM even after attempt on shortening the history: " + retry_response.text)
                        return ""

                logger.error("Failed to call LLM: " + response.text)
                time.sleep(5)
                return ""
            else:
                usage = response.json()["usage"]
                self.usages["prompt_tokens"] += usage["prompt_tokens"]
                self.usages["completion_tokens"] += usage["completion_tokens"]
                return response.json()['choices'][0]['message']['content']

        elif self.model.startswith("claude"):
            messages = payload["messages"]
            max_tokens = payload["max_tokens"]
            top_p = payload["top_p"]
            temperature = payload["temperature"]

            claude_messages = []

            for i, message in enumerate(messages):
                claude_message = {
                    "role": message["role"],
                    "content": []
                }
                assert len(message["content"]) in [1, 2], "One text, or one text with one image"
                for part in message["content"]:

                    if part['type'] == "image_url":
                        image_source = {}
                        image_source["type"] = "base64"
                        image_source["media_type"] = "image/png"
                        image_source["data"] = part['image_url']['url'].replace("data:image/png;base64,", "")
                        claude_message['content'].append({"type": "image", "source": image_source})

                    if part['type'] == "text":
                        claude_message['content'].append({"type": "text", "text": part['text']})

                claude_messages.append(claude_message)

            # the claude not support system message in our endpoint, so we concatenate it at the first user message
            if claude_messages[0]['role'] == "system":
                claude_system_message_item = claude_messages[0]['content'][0]
                claude_messages[1]['content'].insert(0, claude_system_message_item)
                claude_messages.pop(0)

            logger.debug("CLAUDE MESSAGE: %s", repr(claude_messages))

            headers = {
                'Accept': 'application/json',
                'Authorization': f'Bearer {os.environ["ANTHROPIC_API_KEY"]}',
                'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
                'Content-Type': 'application/json'
            }

            payload = {
                "model": self.model,
                "max_tokens": max_tokens,
                "messages": claude_messages,
                "temperature": temperature,
                "top_p": top_p
            }

            max_attempts = 20
            attempt = 0
            while attempt < max_attempts:
                try:
                    response = requests.post(
                        "https://api.claude-Plus.top/v1/chat/completions",
                        headers=headers,
                        json=payload
                    )
                    logger.info(f"response_code {response.status_code}")
                except:
                    time.sleep(8)
                    continue
                if response.status_code == 200:
                    result = response.json()['choices'][0]['message']['content']
                    break
                else:
                    logger.error(f"Failed to call LLM", response.json())
                    if "found multiple" in response.json()['error']['message']:
                        logger.error(f"Fail")
                        if claude_messages[-1]['role'] == 'user' and claude_messages[-2]['role'] == 'user':
                            claude_messages[-2]['content'][0]['text'] = claude_messages[-2]['content'][0]['text'] + " " + claude_messages[-1]['content'][0]['text']
                            claude_messages.pop(-1)
                            payload['messages'] = claude_messages
                            response = requests.post(
                                "https://api.claude-Plus.top/v1/chat/completions",
                                headers=headers,
                                json=payload
                            )
                            result = response.json()['choices'][0]['message']['content']
                            break
                    else:
                        time.sleep(10)
                    attempt += 1
            else:
                print("Exceeded maximum attempts to call LLM.")
                result = ""
                
            return result

        elif self.model.startswith("mixtral"):
            messages = payload["messages"]
            max_tokens = payload["max_tokens"]
            top_p = payload["top_p"]
            temperature = payload["temperature"]

            mistral_messages = []

            for i, message in enumerate(messages):
                mistral_message = {
                    "role": message["role"],
                    "content": ""
                }

                for part in message["content"]:
                    mistral_message['content'] = part['text'] if part['type'] == "text" else ""

                mistral_messages.append(mistral_message)

            from openai import OpenAI

            client = Groq(
                api_key=os.environ.get("GROQ_API_KEY"),
            )

            flag = 0
            while True:
                try:
                    if flag > 20:
                        break
                    logger.info("Generating content with model: %s", self.model)
                    response = client.chat.completions.create(
                        messages=mistral_messages,
                        model=self.model,
                        max_tokens=max_tokens,
                        top_p=top_p,
                        temperature=temperature
                    )
                    break
                except:
                    if flag == 0:
                        mistral_messages = [mistral_messages[0]] + mistral_messages[-1:]
                    else:
                        mistral_messages[-1]["content"] = ' '.join(mistral_messages[-1]["content"].split()[:-500])
                    flag = flag + 1

            try:
                return response.choices[0].message.content
            except Exception as e:
                print("Failed to call LLM: " + str(e))
                return ""

        elif self.model.startswith("THUDM"):
            # THUDM/cogagent-chat-hf
            messages = payload["messages"]
            max_tokens = payload["max_tokens"]
            top_p = payload["top_p"]
            temperature = payload["temperature"]

            cog_messages = []

            for i, message in enumerate(messages):
                cog_message = {
                    "role": message["role"],
                    "content": []
                }

                for part in message["content"]:
                    if part['type'] == "image_url":
                        cog_message['content'].append(
                            {"type": "image_url", "image_url": {"url": part['image_url']['url']}})

                    if part['type'] == "text":
                        cog_message['content'].append({"type": "text", "text": part['text']})

                cog_messages.append(cog_message)

            # the cogagent not support system message in our endpoint, so we concatenate it at the first user message
            if cog_messages[0]['role'] == "system":
                cog_system_message_item = cog_messages[0]['content'][0]
                cog_messages[1]['content'].insert(0, cog_system_message_item)
                cog_messages.pop(0)

            payload = {
                "model": self.model,
                "max_tokens": max_tokens,
                "messages": cog_messages,
                "temperature": temperature,
                "top_p": top_p
            }

            base_url = "http://127.0.0.1:8000"

            response = requests.post(f"{base_url}/v1/chat/completions", json=payload, stream=False)
            if response.status_code == 200:
                decoded_line = response.json()
                content = decoded_line.get("choices", [{}])[0].get("message", "").get("content", "")
                return content
            else:
                print("Failed to call LLM: ", response.status_code)
                return ""

        elif self.model in ["gemini-pro", "gemini-pro-vision"]:
            messages = payload["messages"]
            max_tokens = payload["max_tokens"]
            top_p = payload["top_p"]
            temperature = payload["temperature"]

            if self.model == "gemini-pro":
                assert self.observation_space in pure_text_settings, f"The model {self.model} can only support text-based input, please consider change based model or settings"

            gemini_messages = []
            for i, message in enumerate(messages):
                role_mapping = {
                    "assistant": "model",
                    "user": "user",
                    "system": "system"
                }
                gemini_message = {
                    "role": role_mapping[message["role"]],
                    "parts": []
                }
                assert len(message["content"]) in [1, 2], "One text, or one text with one image"

                # The gemini only support the last image as single image input
                if i == len(messages) - 1:
                    for part in message["content"]:
                        gemini_message['parts'].append(part['text']) if part['type'] == "text" \
                            else gemini_message['parts'].append(encoded_img_to_pil_img(part['image_url']['url']))
                else:
                    for part in message["content"]:
                        gemini_message['parts'].append(part['text']) if part['type'] == "text" else None

                gemini_messages.append(gemini_message)

            # the gemini not support system message in our endpoint, so we concatenate it at the first user message
            if gemini_messages[0]['role'] == "system":
                gemini_messages[1]['parts'][0] = gemini_messages[0]['parts'][0] + "\n" + gemini_messages[1]['parts'][0]
                gemini_messages.pop(0)

            # since the gemini-pro-vision donnot support multi-turn message
            if self.model == "gemini-pro-vision":
                message_history_str = ""
                for message in gemini_messages:
                    message_history_str += "<|" + message['role'] + "|>\n" + message['parts'][0] + "\n"
                gemini_messages = [{"role": "user", "parts": [message_history_str, gemini_messages[-1]['parts'][1]]}]
                # gemini_messages[-1]['parts'][1].save("output.png", "PNG")

            # print(gemini_messages)
            api_key = os.environ.get("GENAI_API_KEY")
            assert api_key is not None, "Please set the GENAI_API_KEY environment variable"
            genai.configure(api_key=api_key)
            logger.info("Generating content with Gemini model: %s", self.model)
            request_options = {"timeout": 120}
            gemini_model = genai.GenerativeModel(self.model)

            response = gemini_model.generate_content(
                gemini_messages,
                generation_config={
                    "candidate_count": 1,
                    # "max_output_tokens": max_tokens,
                    "top_p": top_p,
                    "temperature": temperature
                },
                safety_settings={
                    "harassment": "block_none",
                    "hate": "block_none",
                    "sex": "block_none",
                    "danger": "block_none"
                },
                request_options=request_options
            )
            return response.text

        elif self.model == "gemini-1.5-pro-latest":
            messages = payload["messages"]
            max_tokens = payload["max_tokens"]
            top_p = payload["top_p"]
            temperature = payload["temperature"]

            gemini_messages = []

            for i, message in enumerate(messages):
                gemini_message = {
                    "role": message["role"],
                    "content": []
                }
                assert len(message["content"]) in [1, 2], "One text, or one text with one image"
                for part in message["content"]:

                    if part['type'] == "image_url":
                        image_source = {}
                        image_source["type"] = "base64"
                        image_source["media_type"] = "image/png"
                        image_source["data"] = part['image_url']['url'].replace("data:image/png;base64,", "")
                        gemini_message['content'].append({"type": "image", "source": image_source})

                    if part['type'] == "text":
                        gemini_message['content'].append({"type": "text", "text": part['text']})

                gemini_messages.append(gemini_message)

            headers = {
                'Accept': 'application/json',
                'Authorization': f'Bearer {os.environ["GEMINI_API_KEY"]}',
                'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
                'Content-Type': 'application/json'
            }  
            
            payload = json.dumps({"model": self.model,"messages": gemini_messages,"max_tokens": max_tokens,"temperature": temperature,"top_p": top_p})

    
            
            max_attempts = 20
            attempt = 0
            while attempt < max_attempts:
                try:
                    response = requests.request("POST", "https://api2.aigcbest.top/v1/chat/completions", headers=headers, data=payload)
                    logger.info(f"response_code {response.status_code}")
                except:
                    time.sleep(5)
                    continue
                if response.status_code == 200:
                    result = response.json()['choices'][0]['message']['content']
                    break
                else:
                    logger.error(f"Failed to call LLM")
                    time.sleep(5)
                    attempt += 1
            else:
                print("Exceeded maximum attempts to call LLM.")
                result = ""
                
            return result

        elif self.model == "llama3-70b":
            messages = payload["messages"]
            max_tokens = payload["max_tokens"]
            top_p = payload["top_p"]
            temperature = payload["temperature"]

            groq_messages = []

            for i, message in enumerate(messages):
                groq_message = {
                    "role": message["role"],
                    "content": ""
                }

                for part in message["content"]:
                    groq_message['content'] = part['text'] if part['type'] == "text" else ""

                groq_messages.append(groq_message)

            # The implementation based on Groq API
            client = Groq(
                api_key=os.environ.get("GROQ_API_KEY"),
            )

            flag = 0
            while True:
                try:
                    if flag > 20:
                        break
                    logger.info("Generating content with model: %s", self.model)
                    response = client.chat.completions.create(
                        messages=groq_messages,
                        model="llama3-70b-8192",
                        max_tokens=max_tokens,
                        top_p=top_p,
                        temperature=temperature
                    )
                    break
                except:
                    if flag == 0:
                        groq_messages = [groq_messages[0]] + groq_messages[-1:]
                    else:
                        groq_messages[-1]["content"] = ' '.join(groq_messages[-1]["content"].split()[:-500])
                    flag = flag + 1

            try:
                return response.choices[0].message.content
            except Exception as e:
                print("Failed to call LLM: " + str(e))
                return ""

        elif self.model.startswith("qwen"):
            messages = payload["messages"]
            max_tokens = payload["max_tokens"]
            top_p = payload["top_p"]
            temperature = payload["temperature"]

            qwen_messages = []

            for i, message in enumerate(messages):
                qwen_message = {
                    "role": message["role"],
                    "content": []
                }
                assert len(message["content"]) in [1, 2], "One text, or one text with one image"
                for part in message["content"]:
                    qwen_message['content'].append({"image": "file://" + save_to_tmp_img_file(part['image_url']['url'])}) if part[
                                                                                                                     'type'] == "image_url" else None
                    qwen_message['content'].append({"text": part['text']}) if part['type'] == "text" else None

                qwen_messages.append(qwen_message)

            flag = 0
            while True:
                try:
                    if flag > 20:
                        break
                    logger.info("Generating content with model: %s", self.model)

                    if self.model in ["qwen-vl-plus", "qwen-vl-max"]:
                        response = dashscope.MultiModalConversation.call(
                            model=self.model,
                            messages=qwen_messages,
                            result_format="message",
                            max_length=max_tokens,
                            top_p=top_p,
                            temperature=temperature
                        )

                    elif self.model in ["qwen-turbo", "qwen-plus", "qwen-max", "qwen-max-0428", "qwen-max-0403",
                                        "qwen-max-0107", "qwen-max-longcontext"]:
                        response = dashscope.Generation.call(
                            model=self.model,
                            messages=qwen_messages,
                            result_format="message",
                            max_length=max_tokens,
                            top_p=top_p,
                            temperature=temperature
                        )

                    else:
                        raise ValueError("Invalid model: " + self.model)

                    if response.status_code == HTTPStatus.OK:
                        break
                    else:
                        logger.error('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
                            response.request_id, response.status_code,
                            response.code, response.message
                        ))
                        raise Exception("Failed to call LLM: " + response.message)
                except:
                    if flag == 0:
                        qwen_messages = [qwen_messages[0]] + qwen_messages[-1:]
                    else:
                        for i in range(len(qwen_messages[-1]["content"])):
                            if "text" in qwen_messages[-1]["content"][i]:
                                qwen_messages[-1]["content"][i]["text"] = ' '.join(
                                    qwen_messages[-1]["content"][i]["text"].split()[:-500])
                    flag = flag + 1

            try:
                if self.model in ["qwen-vl-plus", "qwen-vl-max"]:
                    return response['output']['choices'][0]['message']['content'][0]['text']
                else:
                    return response['output']['choices'][0]['message']['content']

            except Exception as e:
                print("Failed to call LLM: " + str(e))
                return ""

        else:
            raise ValueError("Invalid model: " + self.model)

    def parse_actions(self, response: str, masks=None):

        if self.observation_space in ["screenshot", "a11y_tree", "screenshot_a11y_tree"]:
            # parse from the response
            if self.action_space == "computer_13":
                actions = parse_actions_from_string(response)
            elif self.action_space == "pyautogui":
                actions = parse_code_from_string(response)
            else:
                raise ValueError("Invalid action space: " + self.action_space)

            self.actions.append(actions)

            return actions
        elif self.observation_space in ["som"]:
            # parse from the response
            if self.action_space == "computer_13":
                raise ValueError("Invalid action space: " + self.action_space)
            elif self.action_space == "pyautogui":
                actions = parse_code_from_som_string(response, masks)
            else:
                raise ValueError("Invalid action space: " + self.action_space)

            self.actions.append(actions)

            return actions

    def reset(self):
        self.thoughts = []
        self.actions = []
        self.observations = []
