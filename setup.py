from setuptools import setup
import imaplib2

setup(
    name="imaplib2",
    version=imaplib2.__version__,
    description="A threaded Python IMAP4 client.",
    author="Piers Lauder",
    url="http://sourceforge.net/projects/imaplib2/",
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
    ],
    py_modules=['imaplib2'],
)
