__all__ = ["calc_version", "next_version"]

from packaging.version import Version
from vcs_versioning import ScmVersion


def calc_version(v: ScmVersion) -> Version:
    if v.dirty or v.distance:
        return next_version(v.tag)
    else:
        return v.tag


def from_parts(
    epoch: int = 0,
    release: tuple[int, ...] = (),
    pre: tuple[str, int] | None = None,
    post: int | None = None,
    dev: int | None = None,
    local: str | None = None,
) -> Version:
    return Version.from_parts(epoch=epoch, release=release, pre=pre, post=post, dev=dev, local=local)


def update_parts(
    version: Version,
    *,
    epoch: int | None = None,
    release: tuple[int, ...] | None = None,
    pre: tuple[str, int] | None = None,
    post: int | None = None,
    dev: int | None = None,
    local: str | None = None,
) -> Version:
    if epoch is None:
        epoch = version.epoch
    if release is None:
        release = version.release
    if pre is None:
        pre = version.pre
    if post is None:
        post = version.post
    if dev is None:
        dev = version.dev
    if local is None:
        local = version.local
    return from_parts(epoch, release, pre, post, dev, local)


def next_version(version: Version) -> Version:
    if version.pre is not None:
        type_, i = version.pre
        i += 1
        return update_parts(version, pre=(type_, i))
    vs = list(version.release)
    vs[-1] += 1
    return update_parts(version, release=tuple(vs), pre=("a", 0))
