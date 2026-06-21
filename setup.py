import sys

from setuptools import setup

if sys.version_info >= (3, 11):
    import tomllib
else:
    import tomli as tomllib

sys.path.insert(0, "src")
from gitversion_simple.version import get_with_config

with open("pyproject.toml", "rb") as f:
    data = tomllib.load(f)

version = get_with_config()

setup(
    version=version,
    install_requires=data["dependency-groups"]["requires"],
    extras_require={"setuptools": [f"gitversion_simple_setuptools=={version}"]},
)
