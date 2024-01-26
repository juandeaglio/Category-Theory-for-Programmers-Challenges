"""Tests for composing two functions into each other for a resulting function"""
import time
from typing import TypeVar, Callable
import pytest


usleep = lambda x: time.sleep(x/1000.0)

memoized = {}


def upper_pure_function(func, arg):
    if memoized.get(arg) is None:
        function: Callable[[...], TypeVar] = func
        usleep(500)
        value: TypeVar = function(arg)
        memoized[arg] = value
        return value
    else:
        return memoized.get(arg)


# Implement the composition function in your favorite language. It
# takes two functions as arguments and returns a function that is
# their composition.
def test_composed_function():
    start = time.time()
    retval: str = upper_pure_function(str.upper, "Hello!")
    end = time.time()
    not_memoized_call = end - start

    # now the memoized version
    start = time.time()
    retval2: str = upper_pure_function(str.upper, "Hello!")
    end = time.time()
    memoized_call = end - start

    assert memoized_call < not_memoized_call and retval == retval2
