"""Setup for abacus_mmm value package."""

import os

from setuptools import find_packages
from setuptools import setup

_CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


def _get_readme():
  try:
    readme = open(
        os.path.join(_CURRENT_DIR, "README.md"), encoding="utf-8").read()
  except OSError:
    readme = ""
  return readme


def _get_version():
  with open(os.path.join(_CURRENT_DIR, "abacus_mmm", "__init__.py")) as fp:
    for line in fp:
      if line.startswith("__version__") and "=" in line:
        version = line[line.find("=") + 1:].strip(" '\"\n")
        if version:
          return version
    raise ValueError(
        "`__version__` not defined in `abacus_mmm/__init__.py`")


def _parse_requirements(path):

  with open(os.path.join(_CURRENT_DIR, path)) as f:
    return [
        line.rstrip()
        for line in f
        if not (line.isspace() or line.startswith("#"))
    ]

_VERSION = _get_version()
_README = _get_readme()
_INSTALL_REQUIREMENTS = _parse_requirements(os.path.join(
    _CURRENT_DIR, "requirements", "requirements.txt"))
_TEST_REQUIREMENTS = _parse_requirements(os.path.join(
    _CURRENT_DIR, "requirements", "requirements_tests.txt"))

setup(
    name="abacus_mmm",
    version=_VERSION,
    description="Package for Media-Mix-Modelling",
    long_description="\n".join([_README]),
    long_description_content_type="text/markdown",
    author="Google LLC",
    author_email="no-reply@google.com",
    license="Apache 2.0",
    packages=find_packages(),
    install_requires=_INSTALL_REQUIREMENTS,
    tests_require=_TEST_REQUIREMENTS,
    url="https://github.com/google/abacus_mmm",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",

    ],
)
