"""Tests for composing two functions into each other for a resulting function"""
import math
import random
import time
from typing import TypeVar, Callable
import pytest

usleep = lambda x: time.sleep(x / 1000.0)

memoized = {}

T = TypeVar('T')


def memoize_slow_function(func, *argv):
    if memoized.get(argv) is None:
        usleep(500)

    result = memoize_function(func, *argv)
    return result


def memoize_function(func, *argv):
    if memoized.get(argv) is None:
        function: Callable[[...], T] = func
        value: T = function(*argv)
        memoized[argv] = value
        return value

    return memoized.get(argv)


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


def test_memoize_slow_pow():
    start = time.time()
    retval: str = memoize_slow_function(math.pow, 2, 2)
    end = time.time()
    not_memoized_call = end - start

    # now the memoized version
    start = time.time()
    retval2: str = memoize_slow_function(math.pow, 2, 2)
    end = time.time()
    memoized_call = end - start

    assert memoized_call < not_memoized_call and retval == retval2 and retval2 == 4


def test_memoize_random_no_args():
    not_memoized = memoize_function(random.random)
    memoized = memoize_function(random.random)

    epsilon = 1 / math.pow(10, 5)
    assert pytest.approx(memoized, epsilon) == pytest.approx(not_memoized, epsilon)


def seeded_random(seed):
    random.seed = seed
    return random.random()


def test_memoize_seeded_random_with_time():
    not_memoized = memoize_function(seeded_random, time.time())
    memoized = memoize_function(seeded_random, time.time())

    epsilon = 1 / math.pow(10, 5)
    assert pytest.approx(memoized, epsilon) == pytest.approx(not_memoized, epsilon)


def test_memoize_factorial():
    factorial_to = 10
    not_memoized = memoize_function(math.factorial, factorial_to)
    memoized = memoize_function(math.factorial, factorial_to)

    assert not_memoized == memoized


def test_memoize_getchar():
    not_memoized = memoize_function(input)
    memoized = memoize_function(input)

    assert not_memoized == memoized


def bool_func_with_print():
    print("Hello!")
    return True


def test_memoize_bool_with_side_effect():
    not_memoized = memoize_function(bool_func_with_print)
    memoized = memoize_function(bool_func_with_print)

    assert not_memoized == memoized

