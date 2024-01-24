"""Tests for composing two functions into each other for a resulting function"""
from typing import TypeVar, Callable
import pytest


@pytest.fixture
def function_argument_fixture():
    a: int
    a = 2
    return a


def test_composed_function(function_argument_fixture):
    T = TypeVar('T')

    def func(x: int):
        return x + 3

    def func2(x: int):
        return x + 4

    composed: Callable[[T], T] = lambda x: func2(func(x))

    assert composed(function_argument_fixture) == 9


def compose(f, g, x):
    return f(g(x))

def test_composed_function_is_identity():
    identity: Callable[[int], int] = lambda x: x

    def square(x: int):
        return pow(x, 2)

    def cube(x: int):
        return pow(x, 3)

    result = compose(square, cube, 1)

    assert result == identity(1)


def test_composed_function_is_not_identity(function_argument_fixture):
    identity: Callable[[int], int] = lambda x: x

    def square(x: int):
        return pow(x, 2)

    def cube(x: int):
        return pow(x, 3)

    result = compose(square, cube, function_argument_fixture)

    assert result != identity(function_argument_fixture)
