__all__ = ["find"]
from os import PathLike

from vcs_versioning import Configuration, ScmVersion


def find(directory: str | PathLike[str]) -> ScmVersion | None:
    config = Configuration(root=directory)
    wd = config.discover_workdir()
    if wd is None:
        return None
    return wd.get_scm_version()
