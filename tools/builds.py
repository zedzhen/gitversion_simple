import sys
from contextlib import chdir
from pathlib import Path

from build.env import DefaultIsolatedEnv

from build import ProjectBuilder

base_dir = Path(__file__).resolve().parent.parent

out = "dist/"

if "--one-out" in sys.argv:
    out_compat = Path("dist/").resolve()
else:
    out_compat = "dist/"

with chdir(base_dir):
    with DefaultIsolatedEnv() as env:
        builder = ProjectBuilder(".", env.python_executable)
        env.install(builder.build_system_requires)

        builder.build("sdist", out)
        wheel_file = builder.build("wheel", out)

    with chdir("compat/setuptools"), DefaultIsolatedEnv() as env:
        builder = ProjectBuilder(".", env.python_executable)
        env.install([wheel_file])
        env.install(builder.build_system_requires)

        builder.build("sdist", out_compat)
        builder.build("wheel", out_compat)
