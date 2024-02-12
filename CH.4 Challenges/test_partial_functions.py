import math
import pytest
import unittest
from fractions import Fraction
from typing import TypeVar, Callable, Type, Union, Optional

import pytest

T = TypeVar('T')


# Question 1
class Partial:
    def __init__(self, t: Type[T], _value=None):
        if _value is not None:
            assert isinstance(_value, t)
            self._value = _value
            self._is_valid = True
        else:
            self._is_valid = False
            self._value = None

    def value(self):
        return self._value

    def is_valid(self):
        return self._is_valid


def safe_reciprocal(x: Fraction) -> Partial(Fraction):
    if x:
        assert isinstance(x, Fraction)
        if x.numerator != 0:
            # take reciprocal
            reciprocal = Fraction(numerator=x.denominator, denominator=x.numerator)
            return Partial(Fraction, reciprocal)

    return Partial(Fraction)


def identity(x: Partial) -> Partial:
    return x


def compose_functions(f: Callable, g: Callable) -> Callable:
    def composed_functions(x: any):
        # Apply function f to input x
        res_f = f(x)

        # Apply function g to the result of f
        res_g = g(res_f.value())

        return res_g

    return composed_functions


def safe_root(x: Union[int, float, Fraction]) -> Partial(float):
    if x:
        value = x
        assert isinstance(x, (int, float, Fraction))
        # Fraction support
        if isinstance(x, Fraction):
            value = x.real
        if x >= 0:
            return Partial(float, math.sqrt(value))

    return Partial(float)


def is_natural_number(x: int) -> Partial(int):
    if x:
        assert isinstance(x, int)
        if x >= 0:
            return Partial(int, x)

    return Partial(int)


class MyTestCase(unittest.TestCase):
    def test_create_partial_sqrt_function(self):
        assert safe_root(1).value() == 1
        assert not safe_root(-1).is_valid()

    def test_natural_number_function(self):
        assert not is_natural_number(-1).is_valid()
        assert is_natural_number(-1).value() is None
        assert is_natural_number(1).value() == 1

    def test_identity_partial_empty_function(self):
        assert identity(Partial(int)).is_valid() is False
        assert identity(Partial(int, 1)).is_valid() is True

    def test_compose_partial_functions(self):
        composed_function = compose_functions(is_natural_number, safe_root)

        assert 1 == composed_function(1).value()
        assert not composed_function(-1).is_valid()
        assert 2 == composed_function(4).value()

    # Question 2
    def test_safe_reciprocal(self):
        assert 1 == safe_reciprocal(Fraction(1.0)).value()
        assert not safe_reciprocal(Fraction(0.0)).is_valid()

    # Question 3
    def test_compose_reciprocal_sqrt(self):
        composed: Callable = compose_functions(safe_reciprocal, safe_root)

        result: Partial = composed(Fraction(math.pi))
        assert result.is_valid()

        expected: float = math.sqrt(1/math.pi)
        assert pytest.approx(expected) == pytest.approx(result.value())

if __name__ == '__main__':
    unittest.main()
