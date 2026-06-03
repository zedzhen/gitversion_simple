A simple version based on git for setuptools.

If there have been no commits or uncommitted changes since the most recent tag,
the version from the tag is used as the project version.

If the latest tag is final release, then the last part is incremented by 1 and alpha 0 is added.

If the latest tag is pre-release, the pre-release number is incremented by 1.

used:
1. add "gitversion_simple" in build-system.requires (in pyproject.toml)
    ```toml
    [build-system]
    requires = [
        "setuptools>=81.0.0",
        "gitversion_simple~=1.1",
    ]
    ```
2. add in pyproject.toml
    ```toml
   [tool.versioningit.next-version]
    method = "simple"
    
    [tool.versioningit.format]
    method = "simple"
    ```

examples:

| last tag | version |
|----------|---------|
| v1.0.0   | 1.0.1   | 
| v1.0.0a1 | 1.0.0a2 |
| v1.0.0b2 | 1.0.0b3 |
| v1.0     | 1.1     |
| v1.2.3.4 | 1.2.3.5 |
| v26.1    | 26.2    |
