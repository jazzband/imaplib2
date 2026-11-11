import datetime
import re
import time

import pytest

from imaplib2 import Time2Internaldate

# Format: "DD-Mmm-YYYY HH:MM:SS +HHMM"
INTERNALDATE_PATTERN = re.compile(
    r'^"[0-3]\d-(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)-\d{4} \d{2}:\d{2}:\d{2} [+-]\d{4}"$'
)


def test_time2internaldate_float():
    ts = time.time()
    result = Time2Internaldate(ts)
    assert INTERNALDATE_PATTERN.match(result)


def test_time2internaldate_int():
    ts = int(time.time())
    result = Time2Internaldate(ts)
    assert INTERNALDATE_PATTERN.match(result)


def test_time2internaldate_struct_time():
    st = time.localtime()
    result = Time2Internaldate(st)
    assert INTERNALDATE_PATTERN.match(result)


def test_time2internaldate_tuple():
    st_tuple = time.localtime()[:9]
    result = Time2Internaldate(st_tuple)
    assert INTERNALDATE_PATTERN.match(result)


def test_time2internaldate_aware_datetime():
    dt = datetime.datetime.now(datetime.timezone.utc)
    result = Time2Internaldate(dt)
    assert INTERNALDATE_PATTERN.match(result)
    assert result.endswith(' +0000"')


def test_time2internaldate_quoted_string():
    raw = '"07-Nov-2026 12:00:00 +0000"'
    assert Time2Internaldate(raw) == raw


def test_time2internaldate_naive_datetime():
    naive = datetime.datetime(2026, 11, 7, 12, 0, 0, tzinfo=None)  # noqa: DTZ001
    with pytest.raises(ValueError, match="date_time must be aware"):
        Time2Internaldate(naive)


def test_time2internaldate_invalid_type():
    with pytest.raises(ValueError, match="date_time not of a known type"):
        Time2Internaldate(object())
