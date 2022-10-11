import sys

from setuptools import setup

increment = int(sys.argv.pop())
name = "types-tsbot-empty"
description = "Empty typing stubs for testing typeshed/PyPI auto-upload"

setup(
    name=name,
    version=f"0.1.{increment}",
    description=description,
    long_description=description,
    url="https://github.com/typeshed-internal/stub_uploader",
    install_requires=[],
    packages=[],
    classifiers=[
        "Typing :: Stubs Only",
    ],
)
