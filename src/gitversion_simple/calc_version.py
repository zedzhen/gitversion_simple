__all__ = ["calc_version"]

from gitversion_simple.next_version import next_version
from packaging.version import Version
from vcs_versioning import ScmVersion


def calc_version(v: ScmVersion) -> Version:
    if v.dirty or v.distance:
        return next_version(v.tag)
    else:
        return v.tag
