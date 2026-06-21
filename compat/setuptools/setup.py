from setuptools import Distribution, setup

from gitversion_simple.integrations.setuptools_ import finalize_distribution_options

_finalize_options = Distribution.finalize_options


def finalize_options(self: Distribution) -> None:
    _finalize_options(self)
    finalize_distribution_options(self)


Distribution.finalize_options = finalize_options

setup()
