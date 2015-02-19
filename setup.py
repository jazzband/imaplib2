#!/usr/bin/env python
# from distutils.core import setup
from setuptools import setup, find_packages

try:
    from distutils.command.build_py import build_py_2to3 as build_py
except ImportError:
    from distutils.command.build_py import build_py

setup(
    name="imaplib2",
    version="2.38.0",
    description="A threaded Python IMAP4 client.",
    author="Piers Lauder",
    url="http://github.com/bcoe/imaplib2",
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3"
    ],
    packages=find_packages(),
    cmdclass={'build_py': build_py}
)
