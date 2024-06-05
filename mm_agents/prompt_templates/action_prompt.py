#coding=utf8

# We remove some actions to simplify the action space, including RIGHT_CLICK, DOUBLE_CLICK, MOUSE_UP, MOUSE_DOWN, KEY_UP, KEY_DOWN
# RIGHT_CLICK and DOUBLE_CLICK can be implemented by a single CLICK action (specify parameters)
# MOUSE_UP and MOUSE_DOWN are often used in dragging, that is DRAG_TO = MOUSE_DOWN + MOVE_TO + MOUSE_DOWN, thus we only preserve DRAG_TO
# KEY_UP and KEY_DOWN are often used in hot keys, thus, we only preserve actions PRESS and HOTKEY
# In total, 7 + 3 = 10 actions are kept
COMPUTER13_ACTION_SPACE_PROMPT = """
## Action Space

Firstly, we use json dict to describe the types and parameters for each action we allowed (`required=true` means this argument must be provided). Then, we demonstrate use cases, followed by precautions.

### Specification for All Actions

ACTION_LIST = [
    {
        "action_type": "MOVE_TO",
        "note": "move the cursor to a specified position (x, y)",
        "parameters": {
            "x": {
                "type": float,
                "range": [0, MAX_SCREEN_WIDTH],
                "required": true,
            },
            "y": {
                "type": float,
                "range": [0, MAX_SCREEN_HEIGHT],
                "required": true,
            }
        }
    },
    {
        "action_type": "CLICK",
        "note": "click the left button at the current position once if no parameter is specified, otherwise, click the `button` at position (`x`, `y`) for `num_clicks` times",
        "parameters": {
            "button": {
                "type": str,
                "range": ["left", "right", "middle"],
                "default": "left",
            },
            "x": {
                "type": float,
                "range": [0, MAX_SCREEN_WIDTH],
                "default": CURRENT_MOUSE_X_POSITION,
            },
            "y": {
                "type": float,
                "range": [0, MAX_SCREEN_HEIGHT],
                "default": CURRENT_MOUSE_Y_POSITION,
            },
            "num_clicks": {
                "type": int,
                "range": [1, 2, 3],
                "default": 1,
            },
        }
    },
    {
        "action_type": "DRAG_TO",
        "note": "drag the cursor from the current position to the specified position (`x`, `y`) with the left button pressed all the time",
        "parameters": {
            "x": {
                "type": float,
                "range": [0, MAX_SCREEN_WIDTH],
                "required": true,
            },
            "y": {
                "type": float,
                "range": [0, MAX_SCREEN_HEIGHT],
                "required": true,
            }
        }
    },
    {
        "action_type": "SCROLL",
        "note": "scroll the mouse wheel up or down, where `clicks` represents the number of 'clicks' to scroll. And a positive value means scroll up, while a negative value means scroll down",
        "parameters": {
            "clicks": {
                "type": int,
                "required": true,
            }
        }
    },
    {
        "action_type": "TYPING",
        "note": "type the specified text",
        "parameters": {
            "text": {
                "type": str,
                "required": true,
            }
        }
    },
    {
        "action_type": "PRESS",
        "note": "press the specified key and release it",
        "parameters": {
            "key": {
                "type": str,
                "range": KEYBOARD_KEYS,
                "required": true,
            }
        }
    },
    {
        "action_type": "HOTKEY",
        "note": "press the specified key combination, e.g., keys = [\"ctrl\", \"c\"]",
        "parameters": {
            "keys": {
                "type": List[str],
                "range": List[KEYBOARD_KEYS],
                "required": true,
            }
        }
    },
    # THE FOLLOWING ARE 3 SPECIAL ACTIONS YOU WILL USE
    {
        "action_type": "WAIT",
        "note": "wait until the next action, designed for action execution and environment response delay",
    },
    {
        "action_type": "FAIL",
        "note": "decide the task can not be completed",
    },
    {
        "action_type": "DONE",
        "note": "decide the task has been finished",
    }
]

### Use Cases

For example:

- For MOVE_TO, you need to predict the x and y coordinate of the mouse cursor, the left top corner of the screen is (0, 0), the right bottom corner of the screen is determined by the screen size.
Use case: move the mouse to position (56.1, 65.0)
```json
{
    "action_type": "MOVE_TO",
    "x": 56.1,
    "y": 65.0
}
```

- For CLICK, you can specify the `button`, postion (`x` and `y`) and `num_clicks` as well
Use case 1: click the left button once at position (325.2, 401.4)
```json
{
    "action_type": "CLICK",
    "x": 325.2,
    "y": 401.4
}
```
Use case 2: click the right button once at the current position
```json
{
    "action_type": "CLICK",
    "button": "right"
}
```
Use case 3: double click the left button at the current position
```json
{
    "action_type": "CLICK",
    "num_clicks": 2
}
```

- For DRAG_TO, this is equivalent to the combination of mouse down -> move to (`x`, `y`) -> mouse up
Use case: drag the file under the current mouse position to coordiate (235.6, 268.9)
```json
{
    "action_type": "DRAG_TO",
    "x": 235.6,
    "y": 268.9
}
```

- For SCROLL, the parameter `clicks` quantifies the number of discrete wheel events, with each event representing a small incremental movement
Use case: scroll down the current web page by 3 clicks (down -> negative int, up -> positive int)
```json
{
    "action_type": "SCROLL",
    "clicks": -3
}
```

- For TYPING, you need to specify the text you want to type
Use case: type text "hello word" in the current focused input box
```json
{
    "action_type": "TYPING",
    "text": "hello world"
}
```

- For PRESS or HOTKEY, you need to choose one/multiple key(s) from the keyboard
Use case 1: press the Enter key
```json
{
    "action_type": "PRESS",
    "key": "enter"
}
```
Use case 2: press the hot key combination `Ctrl+A` to select all elements on the screen
```json
{
    "action_type": "HOTKEY",
    "keys": ["ctrl", "a"]
}
```

- For the other 3 special actions, no parameter is needed
Use case 1: the program is still running, wait for the termination
```json
{
    "action_type": "WAIT"
}
```
Use case 2: the task has been completed, no action is needed
```json
{
    "action_type": "DONE"
}
```

### Precautions

REMEMBER THAT:
1) The output action MUST BE CHOSEN and CAN ONLY BE CHOSEN from the action space (json dict) defined above, otherwise your action will be considered as invalid and you will get a penalty. For example, bash, sql, or python code WILL NOT be executed;
2) For each action dict, STRICTLY OBEY THE FORMAT, which must contain the `action_type` field and required parameters. Optional parameters will be set to default values if not provided. NEVER RETURN ME ANYTHING ELSE WHICH IS NOT DEFINED;
3) For parameters of each action, pleae STRICTLY CONFORM TO the type and format, e.g., for float types, use float numbers `110` instead of math expression `100 + 20 / 2`;
4) JSON keys and string-type values in the action dict MUST be wrapped with DOUBLE QUOTES \" instead of single quote \' to ensure successful json parsing;
5) The json dict for each action MUST be wrapped with ```json and ``` for clear boundary detection;
6) For efficiency, you CAN predict multiple actions in one response, but REMEMBER TO WRAP EACH ACTION DICT SEPARATELY using backticks ```json and ```.
""".strip()


PYAUTOGUI_ACTION_SPACE_PROMPT = """
## Action Space

You are required to use `pyautogui` to perform the action grounded to the observation. And the action space includes two types:
1. Python code block using pyautogui wrapped by 3 backticks, e.g.,
```python
# you python code here, e.g.,
pyautogui.hotkey('ctrl', 'c')
```
2. Three pre-defined special actions: [WAIT, FAIL, DONE]
- When you think you have to wait for some time, return ```WAIT```;
- When you think the task can not be done, return ```FAIL```, don't easily say ```FAIL```, try your best to do the task;
- When you think the task is done, return ```DONE```.
These 3 actions also need to be wrapped by 3 backticks.

REMEMBER THAT:
0. We will import libraries `pyautogui` and `time` automatically for you, but if you use other python libraries, PLEASE IMPORT THEM FIRST ALTHOUGH THIS IS DISCOURAGED;
1. DONOT use the `pyautogui.locateCenterOnScreen` function to locate the element you want to operate with, since we have no image of the element you want to operate with;
2. DONOT use the `pyautogui.screenshot` function to make screenshot;
3. For time efficiency, you can return one line or multiple lines of python code to perform continuous actions in one response. For example, your response may contain the following code block:
```
pyautogui.moveTo(100, 210)
pyautogui.dragTo(500, 200, button='left', mouseDownUp=True)
pyautogui.rightClick()
```
4. When predicting multiple lines of code, make some small delay like `time.sleep(0.5)` interval, such that the machine can response correctly. And it is STRONGLY RECOMMENDED that, for one action which may influence the environment significantly (e.g., click the button of one application to open it, or click a web link which navigates to a new page), it is better to predict this action without follow-ups in order to observe the changes in environment states first;
5. Each time when you predict code, neither variables nor function is shared acrossed different code blocks. In other words, each code block will be executed in isolation;
6. For coordinates (x, y), please speculate or calculate by yourself based on the observation of previous interaction turn. BE CAREFUL to ensure the coordinates are feasible.
7. Please pay attention that, code wrapped by 3 backticks ``` will be recognized as an action in the action space. Therefore, when you output non-action code, please use other symbols like ''' instead.
""".strip()


SOM_PYAUTOGUI_ACTION_SPACE_PROMPT = """
## Action Space

You are required to use `pyautogui` to perform the action grounded to the observation. And the action space includes two types:
1. Python code block using pyautogui wrapped by 3 backticks, e.g.,
```python
# you python code here, e.g.,
pyautogui.hotkey('ctrl', 'c')
```
Syntax sugar: you can use variable `index_{i}` to represent the CENTER position, namely tuple (x, y), of the i-th element marked in the previous observation space. We will resolve the concrete coordinates for you during execution. For example, the following code represent clicking the center position of the element with index 1 in the labeled screenshot or textual accessibility tree:
```
pyautogui.click(index_1)
```
2. Three pre-defined special actions: [WAIT, FAIL, DONE]
- When you think you have to wait for some time, return ```WAIT```;
- When you think the task can not be done, return ```FAIL```, don't easily say ```FAIL```, try your best to do the task;
- When you think the task is done, return ```DONE```.
These 3 actions also need to be wrapped by 3 backticks.

REMEMBER THAT:
0. We will import libraries `pyautogui` and `time` automatically for you, but if you use other python libraries, PLEASE IMPORT THEM FIRST ALTHOUGH THIS IS DISCOURAGED;
1. DONOT use the `pyautogui.locateCenterOnScreen` function to locate the element you want to operate with, since we have no image of the element you want to operate with;
2. DONOT use the `pyautogui.screenshot` function to make screenshot;
3. For time efficiency, you can return one line or multiple lines of python code to perform continuous actions in one response. For example, your response may contain the following code block:
```
pyautogui.moveTo(100, 210)
pyautogui.dragTo(index_2, button='left', mouseDownUp=True)
pyautogui.rightClick()
```
4. When predicting multiple lines of code, make some small delay like `time.sleep(0.5)` interval, such that the machine can response correctly. And it is STRONGLY RECOMMENDED that, for one action which may influence the environment significantly (e.g., click the button of one application to open it, or click a web link which navigates to a new page), it is better to predict this action without follow-ups in order to observe the changes in environment states first;
5. Each time when you predict code, neither variables nor function is shared acrossed different code blocks. In other words, each code block will be executed in isolation;
6. For coordinates (x, y), please speculate or calculate by yourself based on the observation of previous interaction turn. BE CAREFUL to ensure the coordinates are feasible. You can also take advantage of our provided syntax sugar `index_{i}` to avoid miscalculating the center position.
"""

ACTION_SPACE_PROMPTS = {
    "computer_13": COMPUTER13_ACTION_SPACE_PROMPT,
    "pyautogui": PYAUTOGUI_ACTION_SPACE_PROMPT,
    "pyautogui_som": SOM_PYAUTOGUI_ACTION_SPACE_PROMPT
}