"""Prompt bundle for the LIBERO environment."""
from __future__ import annotations

from physical_agent.envs.base import PromptBundle
from physical_agent.context.loader import read_text_resource

_COMMON_PROMPTS = "physical_agent.context.prompts"

_TOKEN_VALUES = {
    "@ENV_EXPERIMENT_NAME@": "LIBERO PRO",
    "@ENV_DISPLAY_NAME@": "LIBERO PRO",
    "@ENV_NAME@": "LIBERO",
    "@SUCCESS_CONDITION@": "state.libero_terminated == True",
    "@STATE_TERMINATION_FIELD@": "state.libero_terminated",
    "@TERMINATION_FIELD@": "libero_terminated",
    "@STRICT_GUIDE_PATH@": (
        "physical_agent/envs/libero/guides/STRICT_HYBRID_GUIDE.md"
    ),
    "@STRICT_PERCEPTION_GUIDE_PATH@": (
        "physical_agent/envs/libero/guides/STRICT_HYBRID_GUIDE_PERCEPTION.md"
    ),
    "@PRO_GUIDE_PATH@": "physical_agent/envs/libero/guides/PRO_HYBRID_GUIDE.md",
    "@ENV_CALIBRATION_GUIDE_PATH@": (
        "physical_agent/envs/libero/guides/env_calibration.md"
    ),
}


def _prompt(name: str) -> str:
    text = read_text_resource(_COMMON_PROMPTS, name)
    for old, new in _TOKEN_VALUES.items():
        text = text.replace(old, new)
    return text


def format_claude_code_prompt(
    template: str,
    *,
    suite: str,
    task: int,
    seed: int,
    recipe_tag: str,
    output_dir: str,
) -> str:
    """Substitute CLI prompt placeholders without ``str.format``.

    The prompt contains JSON examples with literal braces, so using
    ``str.format()`` would require escaping the whole document. Instead we
    do targeted replacements on the legacy ``{UPPER}`` placeholders.
    """
    replacements = {
        "{SUITE}": suite,
        "{TASK}": str(task),
        "{SEED}": str(seed),
        "{TAG}": recipe_tag,
        "{OUTPUT_DIR}": output_dir,
    }
    prompt = template
    for old, new in replacements.items():
        prompt = prompt.replace(old, str(new))
    return prompt


PROMPTS = PromptBundle(
    system_prompt=_prompt("system.md"),
    initial_user_template=_prompt("initial_user.md"),
    perception_prefix=_prompt("perception_prefix.md"),
    perception_user_template=_prompt("perception_user.md"),
    claude_code_prompt_template=_prompt("claude_code.md"),
    claude_code_perception_prompt_template=_prompt("claude_code_perception.md"),
    format_claude_code_prompt=format_claude_code_prompt,
)
