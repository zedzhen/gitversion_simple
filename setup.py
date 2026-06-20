import sys

from setuptools import Distribution, setup

sys.path.insert(0, "src")
from gitversion_simple.integrations.setuptools_ import finalize_distribution_options

_finalize_options = Distribution.finalize_options


def finalize_options(self: Distribution) -> None:
    _finalize_options(self)
    finalize_distribution_options(self)
    self.extras_require = {"setuptools": [f"gitversion_simple_setuptools=={self.metadata.version}"]}


Distribution.finalize_options = finalize_options

setup()
