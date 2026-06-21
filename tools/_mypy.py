import sys
from pathlib import Path
from subprocess import run

base_dir = Path(__file__).resolve().parent.parent

run([sys.executable, "-m", "pip", "install", "pip", "-U"])
run([sys.executable, "-m", "pip", "install", "--group", "types"])
for py_version in ["3.10", "3.11", "3.12", "3.13", "3.14"]:
    print(f"python version: {py_version}")
    run([sys.executable, "-m", "mypy", "--python-version", py_version]).check_returncode()
