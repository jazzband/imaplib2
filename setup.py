#!/usr/bin/env python
# from distutils.core import setup
from setuptools import setup, find_packages

setup(
    name="imaplib2",
    version="3.06.0",
    description="A threaded Python IMAP4 client.",
    author="Piers Lauder",
    url="https://github.com/bcoe/imaplib2",
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3"
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
    ],
    packages=find_packages(),
)
