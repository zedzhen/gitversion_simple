__all__ = ["find"]

from email.parser import HeaderParser
from os import PathLike
from pathlib import Path

from vcs_versioning import Configuration, ScmVersion
from vcs_versioning._scm_version import meta


def find(directory: str | PathLike[str]) -> ScmVersion | None:
    file = Path(directory) / "PKG-INFO"
    try:
        parser = HeaderParser()
        message = parser.parsestr(file.read_text(encoding="utf-8"))
        data = dict(message.items())
        return meta(data["Version"], preformatted=True, config=Configuration(root=directory))
    except Exception:
        return None
