"""Optional dashboard layer for live-monitoring a PhysicalAgent run.

Opt in via ``python cli/main.py --dashboard``; never imported on the normal
CLI path.
"""
from physical_agent.dashboard.server import DashboardServer
from physical_agent.dashboard.state import State

__all__ = ["DashboardServer", "State"]
