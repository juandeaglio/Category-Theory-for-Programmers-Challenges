"""Tests for various implementations of identity functions seen in category theory"""
from typing import Callable

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
    identity: Callable[[int], int] = lambda x: x
    assert identity(variable_fixture) == variable_fixture
