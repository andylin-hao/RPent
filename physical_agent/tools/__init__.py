"""Agent tool declarations, handlers, and result serialization."""

from physical_agent.tools.repl import (  # noqa: F401
    BLOCKED_ACTIONS,
    TOOLS_SPEC,
    TOOL_HANDLERS,
    execute_tool,
    get_tools_spec,
    set_workdir,
    tool_result_to_content_blocks,
)
