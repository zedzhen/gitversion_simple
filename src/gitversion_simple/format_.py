from packaging.version import Version
from typing_extensions import Any
from versioningit import InvalidVersionError, VCSDescription


def format_(*, description: VCSDescription, base_version: str, next_version: str, params: dict[str, Any]) -> str:
    return next_version
