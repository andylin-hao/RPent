"""LIBERO prompt bundle assembly."""
from __future__ import annotations

from physical_agent.context.prompt_utils import PromptNode
from physical_agent.context.prompts import prompt as base_prompt
from physical_agent.envs.libero import prompts as libero_prompt


def system_prompt() -> dict[str, PromptNode]:
    """Return the system prompt tree."""
    return {
        "Intro": libero_prompt.PREAMBLE,
        "Goal": libero_prompt.GOAL,
        "Rules": libero_prompt.RULES,
        "Localization": libero_prompt.LOCALIZATION,
        "Workflow": libero_prompt.WORKFLOW,
        "Environment": libero_prompt.ENVIRONMENT,
        "Output": base_prompt.OUTPUT,
        "Next": libero_prompt.NEXT,
    }


def user_prompt() -> dict[str, PromptNode]:
    """Return the first user message tree."""
    sections = dict(base_prompt.USER)
    sections["Mode"] = libero_prompt.USER_MODE
    return sections
