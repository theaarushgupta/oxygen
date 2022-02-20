from setuptools import setup
from pathlib import Path

code = Path(__file__).parent
requirements = (code / "requirements.txt")

with open(requirements) as requirements:
    requirements = requirements.readlines()
    requirements = [requirement.replace("\n", "") for requirement in requirements]

setup(
    name = "oxygen",
    version = "v0.0.1",
    author = "Aarush Gupta",
    install_requires = requirements,
    entry_points = {
        "console_scripts": ["oxygen = oxygen.main:main"]
    }
)