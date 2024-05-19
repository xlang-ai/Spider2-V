#coding=utf8
from mm_agents.prompt_templates.system_prompt import SYSTEM_PROMPT
from mm_agents.prompt_templates.action_prompt import ACTION_SPACE_PROMPTS
from mm_agents.prompt_templates.observation_prompt import OBSERVATION_SPACE_PROMPTS

__ALL_PROMPTS__ = [
    SYSTEM_PROMPT,
    ACTION_SPACE_PROMPTS,
    OBSERVATION_SPACE_PROMPTS
]