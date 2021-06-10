# imaplib2: a threaded Python IMAP4 client

[![Jazzband](https://jazzband.co/static/img/badge.svg)](https://jazzband.co/)
[![codecov](https://codecov.io/gh/jazzband/imaplib2/branch/master/graph/badge.svg?token=DZZ3P6438E)](https://codecov.io/gh/jazzband/imaplib2)

Based on RFC 3501 and original imaplib module.

This is a version of imaplib that uses threads to allow full use of the
IMAP4 concurrency features, and to de-couple a user of imaplib from i/o
lags, except where explicitly allowed.

Documented in imaplib2.html
