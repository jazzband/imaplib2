#!/usr/bin/env python
#from distutils.core import setup
from setuptools import setup, find_packages

setup(
    name="imaplib2",
    version="2.28.3",
    description="A threaded Python IMAP4 client.",
    author="Piers Lauder",
    url="http://github.com/bcoe/imaplib2",
    classifiers = [
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7"
    ],
    packages = find_packages()
)
