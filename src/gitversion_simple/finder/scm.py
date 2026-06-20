__all__ = ["find"]
from importlib.metadata import entry_points
from os import PathLike

from vcs_versioning import Configuration, ScmVersion
from vcs_versioning.overrides import GlobalOverrides


def find(directory: str | PathLike[str]) -> ScmVersion | None:
    config = Configuration(root=directory)
    with GlobalOverrides.from_env("***"):
        points = entry_points(group="setuptools_scm.parse_scm")
        for point in points:
            f = point.load()
            try:
                v = f(directory, config=config)
            except Exception as e:
                continue
            if isinstance(v, ScmVersion):
                return v
    return None
