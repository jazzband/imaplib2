#!/usr/bin/env python
# from distutils.core import setup
from setuptools import setup, find_packages

setup(
    name="imaplib2",
    version="2.45.0",
    description="A threaded Python IMAP4 client.",
    author="Piers Lauder",
    url="http://github.com/bcoe/imaplib2",
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3"
    ],
    packages=find_packages(),
)
