__all__ = ["finalize_distribution_options"]

from gitversion_simple.config import Config
from gitversion_simple.version import get_version

from setuptools import Distribution


def finalize_distribution_options(dist: Distribution) -> None:
    if dist.metadata.version is None:
        config = Config.from_pyproject()
        dist.metadata.version = str(get_version(config.vcs_root))
