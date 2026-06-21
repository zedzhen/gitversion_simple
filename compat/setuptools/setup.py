from setuptools import setup

from gitversion_simple.version import get_with_config

setup(version=get_with_config())
