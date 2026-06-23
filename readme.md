# EN
[RU](#ru)

A simple version based on git/gh.

If there have been no commits or uncommitted changes since the most recent tag,
the version from the tag is used as the project version.

If the latest tag is final release, then the last part is incremented by 1 and alpha 0 is added.

If the latest tag is pre-release, the pre-release number is incremented by 1.

### used:
add `gitversion_simple[setuptools]` in build-system.requires (in pyproject.toml)
```toml
[build-system]
requires = [
  "setuptools>=81.0.0",
  "gitversion_simple[setuptools]~=3.0",
]
```

If you use a different backend for the build:
1. Add `gitversion_simple` instead of `gitversion_simple[setuptools]`
2. Manually call `gitversion_simple.version.get_version` or `gitversion_simple.version.get_with_config`
3. *If this is a public builder, create a PR/issue to add

This project is based on `vcs-versioning`, so it supports the entry point [`vcs_versioning.discover_workdir`](https://setuptools-scm.readthedocs.io/en/latest/extending/#adding-a-workdir-discovery-factory).

If the file `pyproject.toml` is not located in the root of the repository, then specify the path to the root of the repository in the `vcs_root` parameter in the `tool.gitversion_simple` table.

For the following repository
```text
git_folder/
├─ .git/
├─ my_project
│  ├─ ...
│  └─ pyproject.toml
├─ my_project2
│  ├─ ...
│  └─ pyproject.toml
└ README.md
```
Add to both `pyproject.toml` files
```toml
[tool.gitversion_simple]
vcs_root = ".."
```

### examples:

| last tag | version |
|----------|---------|
| v1.0.0   | 1.0.1   | 
| v1.0.0a1 | 1.0.0a2 |
| v1.0.0b2 | 1.0.0b3 |
| v1.0     | 1.1     |
| v1.2.3.4 | 1.2.3.5 |
| v26.1    | 26.2    |

# RU
[EN](#en)

Простая версия, основанная на git/gh.

Если с момента создания последнего тега не было никаких фиксаций или незафиксированных изменений,
в качестве версии проекта используется версия из тега.

Если последним тегом является финальным релизом, то последняя часть увеличивается на 1 и добавляется alpha 0.

Если последним тегом является предварительным релизом, то номер предварительного выпуска увеличивается на 1.

### Использование:
добавьте `gitversion_simple[setuptools]` в build-system.requires (в файл pyproject.toml)
```toml
[build-system]
requires = [
  "setuptools>=81.0.0",
  "gitversion_simple[setuptools]~=3.0",
]
```

Если вы используете другой бекенд для сборки:
1. Добавьте `gitversion_simple`, вместо `gitversion_simple[setuptools]`
2. Вручную вызовите `gitversion_simple.version.get_version` или `gitversion_simple.version.get_with_config`
3. *Если это публичный сборщик, создайте PR/issue на добавление

Этот проект основан на `vcs-versioning`, поэтому он поддерживает точку входа [`vcs_versioning.discover_workdir`](https://setuptools-scm.readthedocs.io/en/latest/extending/#adding-a-workdir-discovery-factory).

Если файл `pyproject.toml` находиться не в корне репозитория, то укажите путь до корня репозитория в параметре `vcs_root` в таблице `tool.gitversion_simple`.

Для следующего репозитория
```text
git_folder/
├─ .git/
├─ my_project
│  ├─ ...
│  └─ pyproject.toml
├─ my_project2
│  ├─ ...
│  └─ pyproject.toml
└ README.md
```
Добавьте в оба файла `pyproject.toml`
```toml
[tool.gitversion_simple]
vcs_root = ".."
```

### примеры:

| последний тег | версия  |
|---------------|---------|
| v1.0.0        | 1.0.1   | 
| v1.0.0a1      | 1.0.0a2 |
| v1.0.0b2      | 1.0.0b3 |
| v1.0          | 1.1     |
| v1.2.3.4      | 1.2.3.5 |
| v26.1         | 26.2    |
