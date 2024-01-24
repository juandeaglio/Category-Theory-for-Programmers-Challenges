"""Tests for various implementations of identity functions seen in category theory"""
from typing import Callable, TypeVar

import pytest


@pytest.fixture
def variable_fixture():
    a: int
    a = 0
    return a


def untyped_identity(variable_fixture):
    return variable_fixture


def test_untyped_identity(variable_fixture):
    assert untyped_identity(variable_fixture) == variable_fixture


def test_untyped_lambda_identity(variable_fixture):
    assert lambda x: variable_fixture == variable_fixture


def test_typed_lambda_identity(variable_fixture):
    # the type must be an int and return an int
    identity: Callable[[int], int] = lambda x: x
    assert identity(variable_fixture) == variable_fixture


def test_wrong_typed_lambda_identity(variable_fixture):
    # the type must be an int and return an int
    # here, the IDE might give a type hint warning but this is OK for python (scary).
    identity: Callable[[int], int] = lambda x: str(x)
    assert type(identity(variable_fixture)) is not type(variable_fixture)


def test_typed_generic_lambda_identity(variable_fixture):
    # the type is generic
    T = TypeVar('T')
    # lambda with generic types
    identity: Callable[[T], T] = lambda x: x
    assert identity(variable_fixture) == variable_fixture


# if you're concerned about types, assert your code.
def test_wrong_typed_generic_lambda_identity():
    T = TypeVar('T')
    identity: Callable[[T], T] = lambda x: int(x)
    # as you can see, there is no built-in way for type checking aside using asserts
    assert isinstance(identity('123'), int) is not isinstance(identity('123'), str)
