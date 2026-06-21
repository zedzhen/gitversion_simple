__all__ = ["get_version", "get_with_config"]

from collections.abc import Iterable
from os import PathLike

from packaging.version import Version

from gitversion_simple.calc_version import calc_version
from gitversion_simple.config import Config
from gitversion_simple.finder.abc import Finder
from gitversion_simple.finder.smart import find as smart_find


def get_version(directory: str | PathLike[str] = ".", finders: Iterable[Finder] = (smart_find,)) -> Version:
    for finder in finders:
        v = finder(directory)
        if v is not None:
            return calc_version(v)
    raise RuntimeError("Couldn't get version from VCS")


def get_with_config() -> str:
    config = Config.from_pyproject()
    return str(get_version(config.vcs_root))
