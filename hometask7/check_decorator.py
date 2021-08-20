import time
from functools import wraps

import pytest

from hometask7 import log

MISSED_REQUIREMENTS = "Missed requirements"
PASSED_THRESHOLD = "Threshold wasn't exceed"
EXCEED_OR_EQUAL_THRESHOLD = "greater than"


def timeit(threshold=0.0):
    def wrap(function):
        @wraps(function)
        def wrapped_f():
            ts = time.time()
            function()
            te = time.time()
            duration = te - ts
            result = "Threshold wasn't exceed"
            if duration >= threshold:
                result = f"{function.__name__}(duration {duration}) is greater than or equal to the threshold {threshold}"
                log.info(result)
            return result

        return wrapped_f

    return wrap


@pytest.mark.decorator
def test_duration_exceed_threshold():
    @timeit(1)
    def some_function():
        time.sleep(1)

    result = some_function()
    assert EXCEED_OR_EQUAL_THRESHOLD in result, MISSED_REQUIREMENTS


@pytest.mark.decorator
def test_exceed_default_threshold():
    @timeit()
    def some_function():
        time.sleep(1)

    result = some_function()
    assert EXCEED_OR_EQUAL_THRESHOLD in result, MISSED_REQUIREMENTS


@pytest.mark.decorator
def test_duration_less_threshold():
    @timeit(2)
    def some_function():
        time.sleep(0)

    result = some_function()
    assert PASSED_THRESHOLD == result, MISSED_REQUIREMENTS


@pytest.mark.decorator
def test_passed_default_threshold():
    @timeit()
    def some_function():
        time.sleep(0)

    result = some_function()
    assert EXCEED_OR_EQUAL_THRESHOLD in result, MISSED_REQUIREMENTS
