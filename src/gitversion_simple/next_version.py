from packaging.version import Version
from typing_extensions import Any
from versioningit import InvalidVersionError


def from_parts(
    epoch: int = 0,
    release: tuple[int, ...] = (),
    pre: tuple[str, int] | None = None,
    post: int | None = None,
    dev: int | None = None,
    local: str | None = None,
) -> str:
    return str(Version.from_parts(epoch=epoch, release=release, pre=pre, post=post, dev=dev, local=local))


def update_parts(
    version: Version,
    *,
    epoch: int | None = None,
    release: tuple[int, ...] | None = None,
    pre: tuple[str, int] | None = None,
    post: int | None = None,
    dev: int | None = None,
    local: str | None = None,
) -> str:
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


def next_version(*, version: str, branch: str | None = None, params: dict[str, Any]) -> str:
    try:
        v = Version(version)
    except ValueError:
        raise InvalidVersionError(f"Cannot parse version {version!r}")
    if v.pre is not None:
        type_, i = v.pre
        i += 1
        return update_parts(v, pre=(type_, i))
    vs = list(v.release)
    vs[-1] += 1
    return update_parts(v, release=tuple(vs), pre=("a", 0))
