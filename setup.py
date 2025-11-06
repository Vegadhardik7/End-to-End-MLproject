# Responsible to create my machine learning application as a package
# setup.py is a setuptools script that declares a Python package’s metadata, dependencies, entry points, 
# and build/install instructions (legacy; prefer pyproject.toml for new projects).

from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """
    Return list of requirements from a requirements.txt file,
    ignoring empty lines, comments, and editable installs like '-e .'.
    """
    reqs: List[str] = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or line.startswith("-e "):
                continue
            reqs.append(line)
    return reqs



setup(
    name = 'mlproject',
    version = "0.0.1",
    author = "Hardik",
    email = "vegadhardik7@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements("requirements.txt")
)