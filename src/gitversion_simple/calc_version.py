__all__ = ["calc_version"]

from packaging.version import Version
from vcs_versioning import ScmVersion

from gitversion_simple.next_version import next_version


def calc_version(v: ScmVersion) -> Version:
    if v.dirty or v.distance:
        return next_version(v.tag)
    else:
        return v.tag
