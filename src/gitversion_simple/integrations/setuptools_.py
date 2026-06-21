__all__ = ["finalize_distribution_options"]

from setuptools import Distribution

from gitversion_simple.version import get_with_config


def finalize_distribution_options(dist: Distribution) -> None:
    if dist.metadata.version is None:
        dist.metadata.version = get_with_config()
