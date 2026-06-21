import sys

from setuptools import Distribution, setup

if sys.version_info >= (3, 11):
    import tomllib
else:
    import tomli as tomllib

sys.path.insert(0, "src")
from gitversion_simple.integrations.setuptools_ import finalize_distribution_options

_finalize_options = Distribution.finalize_options


def finalize_options(self: Distribution) -> None:
    _finalize_options(self)
    finalize_distribution_options(self)
    self.extras_require = {"setuptools": [f"gitversion_simple_setuptools=={self.metadata.version}"]}
    with open("pyproject.toml", "rb") as f:
        data = tomllib.load(f)
    self.metadata.requires = data["dependency-groups"]["requires"]


Distribution.finalize_options = finalize_options

setup()
