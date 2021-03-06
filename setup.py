#!/usr/bin/env python
import re
from setuptools import setup

try:
    with open("README.md") as fh:
        README = fh.read()
    description = next(s for s in README.splitlines()[2:] if re.match(r"^\w", s))
except (IOError, OSError):
    README = description = ""


setup(
    name="firstwp",
    url="https://github.com/con-f-use/1stworldprobs",
    author="con-f-use",
    author_email="con-f-use@gmx.net",
    description=description,
    long_description=README,
    long_description_content_type="text/markdown",
    use_scm_version=dict(local_scheme=lambda _: ""),
    setup_requires=["setuptools_scm"],
    include_package_data=True,
    zip_safe=True,
    options={"bdist_wheel": {"universal": True}},
    package_dir={"": "src"},
    packages=["firstwp"],
    classifiers=[
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
)
