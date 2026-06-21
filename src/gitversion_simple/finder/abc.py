__all__ = ["Finder"]

from os import PathLike

from typing_extensions import Protocol
from vcs_versioning import ScmVersion


class Finder(Protocol):
    def __call__(self, directory: str | PathLike[str], /) -> ScmVersion | None: ...
