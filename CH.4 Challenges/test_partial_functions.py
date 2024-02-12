import math
import unittest
from typing import TypeVar, Callable, Type

T = TypeVar('T')


class Optional:
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


def identity(x: Type[T]) -> Optional(TypeVar):
    return Optional(x)


def compose_functions(f: Callable, g: Callable) -> Callable:
    def composed_functions(x: any):
        # Apply function f to input x
        res_f = f(x)

        # Apply function g to the result of f
        res_g = g(res_f.value())

        return res_g

    return composed_functions


def safe_root(x: int) -> Optional(float):
    if x:
        assert isinstance(x, int)
        if x >= 0:
            return Optional(float, math.sqrt(x))

    return Optional(float)


def is_natural_number(x: int) -> Optional(int):
    if x:
        assert isinstance(x, int)
        if x >= 0:
            return Optional(int, x)

    return Optional(int)


class MyTestCase(unittest.TestCase):
    def test_create_partial_sqrt_function(self):
        assert safe_root(1).value() == 1
        assert not safe_root(-1).is_valid()

    def test_natural_number_function(self):
        assert not is_natural_number(-1).is_valid()
        assert is_natural_number(-1).value() is None
        assert is_natural_number(1).value() == 1

    def test_identity_partial_empty_function(self):
        assert identity(int).is_valid() is False

    def test_compose_partial_functions(self):
        composed_function = compose_functions(is_natural_number, safe_root)

        assert 1 == composed_function(1).value()
        assert not composed_function(-1).is_valid()
        assert 2 == composed_function(4).value()


if __name__ == '__main__':
    unittest.main()
