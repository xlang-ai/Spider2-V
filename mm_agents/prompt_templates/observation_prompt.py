#codint=utf8

SCREENSHOT_OBSERVATION_SPACE_PROMPT = """
## Observation Space

After each action step, you will get a image-style observation, which is the screenshot of the computer screen. And you need to predict the next action on the computer based on this image.
""".strip()


A11YTREE_OBSERVATION_SPACE_PROMPT = """
## Observation Space

After each action step, you will get a text-style observation, which is extracted and pruned from the accessibility tree based on AT-SPI library. The accessibility tree describes the elements (e.g., panels, icons, buttons, frames, windows, applications) on the computer desktop, as well as its embedded text content, status and positions. For simplicity, we prune the original tree and only extract useful information into a tabular format for you. Here is a quick glance on the observation:

TAG\tNAME\tPOSITION (top-left x & y)\tSIZE (width & height)\tTEXT
menu\tVisual Studio Code\t(99, 0)\t(184, 27)\t''
push-button\tChromium Web Browser\t(0, 33)\t(70, 64)\t''
terminal\tTerminal\t(70, 74)\t(1430, 832)\t'(base) user@ubuntu:~/projects/$'
... more rows ...

, where `TAG` / `NAME` is the element type / name respectively. `POSITION` and `SIZE` together describe the square position of this element on the computer screen. For example, if you want to click one button, you can click any point in the square area defined by `POSITION` and `SIZE`. Assume that the position of this button is (100, 200), and the size is (40, 40), the CENTER of this button is (120, 220), which is calculated by x = 100 + 40 / 2 = 120, y = 200 + 40 / 2 = 220. `TEXT` refers to the text content embedded in the element, e.g., the bash terminal output or texts in an editable input box.

And you will predict the next action of the computer based on the accessibility tree.
""".strip()


SCREENSHOT_A11YTREE_OBSERVATION_SPACE_PROMPT = """
## Observation Space

The observation space is a combination of two sources: 1) image-style screenshot of the desktop, and 2) text-style accessibility tree derived from AT-SPI library.

### Screenshot

After each action step, you will get a image-style observation, which is the screenshot of the computer screen. And you need to predict the next action on the computer based on this image. You can use this image to locate the elements on the screen or check the status of the computer, especially whether the previous action is successful or not.

### Accessibility Tree

The accessibility tree describes the elements (e.g., panels, icons, buttons, frames, windows, applications) on the computer desktop, as well as its embedded text content, status and positions. For simplicity, we prune the original tree and only extract useful information into a tabular format for you. Here is a quick glance on the observation:

TAG\tNAME\tPOSITION (top-left x & y)\tSIZE (width & height)\tTEXT
menu\tVisual Studio Code\t(99, 0)\t(184, 27)\t''
push-button\tChromium Web Browser\t(0, 33)\t(70, 64)\t''
terminal\tTerminal\t(70, 74)\t(1430, 832)\t'(base) user@ubuntu:~/projects/$'
... more rows ...

, where `TAG` / `NAME` is the element type / name respectively. `POSITION` and `SIZE` together describe the square position of this element on the computer screen. For example, if you want to click one button, you can click any point in the square area defined by `POSITION` and `SIZE`. Assume that the position of this button is (100, 200), and the size is (40, 40), the CENTER of this button is (120, 220), which is calculated by x = 100 + 40 / 2 = 120, y = 200 + 40 / 2 = 220. `TEXT` refers to the text content embedded in the element, e.g., the bash terminal output or texts in an editable input box.

You can use the accessibility tree to accurately locate positions of useful elements on the screen and check the concrete textual contents of elements. 

By combining the screenshot and accessibility tree, you should be intelligent to predict the next feasible and meaningful action.
""".strip()


SOM_OBSERVATION_SPACE_PROMPT = """
## Observation Space

The observation space is a combination of two sources: 1) image-style screenshot of the desktop with interact-able elements marked with numerical indexes, and 2) text-style accessibility tree derived from AT-SPI library.

### Labeled Screenshot

After each action step, you will get a image-style observation, which is the screenshot of the computer screen. For ease of locating positions of elements, we extend the original screenshot with index marks. That is, some salient elements which can be interacted with (e.g., a button or editable input box) are marked with line boudaries and numeric indexes. You can use this image to locate the elements on the screen or check the status of the computer, especially whether the previous action is successful or not.

### Accessibility Tree

The accessibility tree describes the elements (e.g., panels, icons, buttons, frames, windows, applications) on the computer desktop, as well as its embedded text content, status and positions. For simplicity, we prune the original tree and only extract useful information into a tabular format for you. Here is a quick glance on the observation:

INDEX\tTAG\tNAME\tPOSITION (top-left x & y)\tSIZE (width & height)\tTEXT
1\tmenu\tVisual Studio Code\t(99, 0)\t(184, 27)\t''
2\tpush-button\tChromium Web Browser\t(0, 33)\t(70, 64)\t''
3\tterminal\tTerminal\t(70, 74)\t(1430, 832)\t'(base) user@ubuntu:~/projects/$'
... more rows ...

, where `INDEX` indicates exactly the numeric label for each element marked in the screenshot. You can use this alignment information to simplify your predicted action. For example, you can use `pyautogui.click(index_2)` to represent clicking the CENTER of the element with index 2 on the screenshot. We will automatically perform the position calculation and substitution for you. `TAG` / `NAME` is the element type / name respectively. `POSITION` and `SIZE` together describe the square position of this element on the computer screen. For example, if you want to click one button, you can click any point in the square area defined by `POSITION` and `SIZE`. Assume that the position of this button is (100, 200), and the size is (40, 40), the CENTER of this button is (120, 220), which is calculated by x = 100 + 40 / 2 = 120, y = 200 + 40 / 2 = 220. `TEXT` refers to the text content embedded in the element, e.g., the bash terminal output or texts in an editable input box.

You can use the accessibility tree to accurately locate positions of useful elements on the screen and check the concrete textual contents of elements. 

By combining the screenshot and accessibility tree, you should be intelligent to predict the next feasible and meaningful action.
""".strip()


OBSERVATION_SPACE_PROMPTS = {
    "screenshot": SCREENSHOT_OBSERVATION_SPACE_PROMPT,
    "a11y_tree": A11YTREE_OBSERVATION_SPACE_PROMPT,
    "screenshot_a11y_tree": SCREENSHOT_A11YTREE_OBSERVATION_SPACE_PROMPT,
    "som": SOM_OBSERVATION_SPACE_PROMPT
}