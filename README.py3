Threaded Python IMAP4 client version 3.02.

Based on RFC 3501 and original imaplib module.

This is a version of imaplib that uses threads to allow full use of the
IMAP4 concurrency features, and to de-couple a user of imaplib from i/o
lags, except where explicitly allowed.

This is a BETA release of a version converted for native Python3 use.

Documented in imaplib.html.py3, but note the removal of argument quoting
compared with the py2 version of imaplib2.

Install imaplib2.py3 into your Python library path (rename as imaplib2.py).
