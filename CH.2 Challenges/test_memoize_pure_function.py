"""Tests for composing two functions into each other for a resulting function"""
import time
from typing import TypeVar, Callable
import pytest

usleep = lambda x: time.sleep(x / 1000.0)

memoized = {}

T = TypeVar('T')


def memoize_slow_function(func, arg):
    if memoized.get(arg) is None:
        usleep(500)

    result = memoize_function(arg, func)
    return result


def memoize_function(arg, func):
    if memoized.get(arg) is None:
        function: Callable[[...], T] = func
        value: T = function(arg)
        memoized[arg] = value
        return value
    else:
        return memoized.get(arg)


# Implement the composition function in your favorite language. It
# takes two functions as arguments and returns a function that is
# their composition.
def test_memoize_slow_function():
    start = time.time()
    retval: str = memoize_slow_function(str.upper, "Hello!")
    end = time.time()
    not_memoized_call = end - start

    # now the memoized version
    start = time.time()
    retval2: str = memoize_slow_function(str.upper, "Hello!")
    end = time.time()
    memoized_call = end - start

    assert memoized_call < not_memoized_call and retval == retval2 and retval == "HELLO!"
