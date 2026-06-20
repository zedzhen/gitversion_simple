__all__ = ["find"]
from os import PathLike

from gitversion_simple.finder.pkg_info import find as pkg_info_finder
from gitversion_simple.finder.scm import find as scm_finder
from vcs_versioning import ScmVersion


def find(directory: str | PathLike[str]) -> ScmVersion | None:
    if (v := scm_finder(directory)) is not None:
        return v
    if (v := pkg_info_finder(".")) is not None:
        return v
    return None
