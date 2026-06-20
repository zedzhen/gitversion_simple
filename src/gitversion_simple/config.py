__all__ = ["Config"]

import sys
from dataclasses import dataclass
from os import PathLike

if sys.version_info >= (3, 11):
    import tomllib
else:
    import tomli as tomllib


@dataclass
class Config:
    vcs_root: str | PathLike[str] = "."

    @classmethod
    def from_pyproject(cls, file: str | PathLike[str] = "pyproject.toml"):
        with open(file, "rb") as f:
            data = tomllib.load(f)
        tool_data = data.get("tool", {}).get("gitversion_simple", {})
        return cls(**tool_data)
