"""Per-run log directory helpers."""
from __future__ import annotations

import datetime
from pathlib import Path

from physical_agent.utils.config import get_repo_root, get_logs_dir


def make_log_dir(
    *,
    suite: str,
    task: int,
    seed: int,
    repo_root: str | Path | None = None,
    timestamp: str | None = None,
) -> Path:
    """Create ``logs/<timestamp>_<suite>_t<task>_s<seed>/``."""
    if repo_root is None:
        repo_root = get_repo_root()
    repo_root = Path(repo_root)

    if timestamp is None:
        timestamp = datetime.datetime.now().strftime("%Y%m%d-%H:%M:%S")
    tag = f"{suite}_t{task}_s{seed}"
    run_dir = get_logs_dir() if repo_root == get_repo_root() else repo_root / "logs"
    run_dir = run_dir / f"{timestamp}_{tag}"
    run_dir.mkdir(parents=True, exist_ok=True)
    return run_dir