# imaplib2: a threaded Python IMAP4 client

[![Jazzband](https://jazzband.co/static/img/badge.svg)](https://jazzband.co/)
[![Coverage Status](https://coveralls.io/repos/github/jazzband/imaplib2/badge.svg?branch=master)](https://coveralls.io/github/jazzband/imaplib2?branch=master)

Based on RFC 3501 and original imaplib module.

This is a version of imaplib that uses threads to allow full use of the
IMAP4 concurrency features, and to de-couple a user of imaplib from i/o
lags, except where explicitly allowed.

Documented in imaplib2.html
