"""Tests for composing two functions into each other for a resulting function"""
from typing import TypeVar, Callable
import pytest


@pytest.fixture
def function_argument_fixture():
    a: int
    a = 2
    return a


def test_untyped_identity(function_argument_fixture):
    T = TypeVar('T')

    def func(x: int):
        return x + 3

    def func2(x: int):
        return x + 4

    composed: Callable[[T], T] = lambda x: func2(func(x))

    assert composed(function_argument_fixture) == 9
