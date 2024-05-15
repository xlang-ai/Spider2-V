#codint=utf8

SCREENSHOT_OBSERVATION_SPACE_PROMPT = """
## Observation Space

After each action step, you will get a image-style observation, which is the screenshot of the computer screen. And you need to predict the next action on the computer based on this image.
""".strip()


A11YTREE_OBSERVATION_SPACE_PROMPT = """
## Observation Space

After each action step, you will get a text-style observation, which is extracted and pruned from the accessibility tree based on AT-SPI library. The accessibility tree describes the elements (e.g., panels, icons, buttons, frames, windows, applications) on the computer desktop, as well as its embedded text content, status and positions. For simplicity, we prune the original tree and only extract useful information into a tabular format for you. Here is a quick glance on the observation:

tag\tname\tposition (top-left x&y)\tsize (w&h)\ttext
menu\tVisual Studio Code\t(99, 0)\t(184, 27)\t''
push-button\tChromium Web Browser\t(0, 33)\t(70, 64)\t''
terminal\tTerminal\t(70, 74)\t(1430, 832)\t'(base) user@ubuntu:~/projects/$'
... more rows ...

, where `tag` / `name` is the element type / name respectively. `position` and `size` together describe the square position of this element on the computer screen. For example, if you want to click one button, you can click any point in the square area defined by `position` and `size`. Assume that the position of this button is (100, 200), and the size is (40, 40), the CENTER of this button is (120, 220), which is calculated by x = 100 + 40 / 2 = 120, y = 200 + 40 / 2 = 220. `text` refers to the text content embedded in the element, e.g., the bash terminal output or texts in an editable input box.

And you will predict the next action of the computer based on the accessibility tree.
""".strip()


SCREENSHOT_A11YTREE_OBSERVATION_SPACE_PROMPT = """
## Observation Space

""".strip()


SOM_OBSERVATION_SPACE_PROMPT = """
## Observation Space
TODO:
""".strip()


OBSERVATION_SPACE_PROMPTS = {
    "screenshot": SCREENSHOT_OBSERVATION_SPACE_PROMPT,
    "a11y_tree": A11YTREE_OBSERVATION_SPACE_PROMPT,
    "screenshot_a11y_tree": SCREENSHOT_A11YTREE_OBSERVATION_SPACE_PROMPT,
    "som": SOM_OBSERVATION_SPACE_PROMPT
}