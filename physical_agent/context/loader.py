"""Shared package-resource text loading helpers."""
from __future__ import annotations

from importlib.resources import files


def read_text_resource(package: str, name: str) -> str:
    return files(package).joinpath(name).read_text(encoding="utf-8")
