import pytest
from typing import Tuple, TypeVar

T = TypeVar('T')
U = TypeVar('U')


def first(pair: Tuple[T, U]) -> T:
    return pair[0]


def second(pair: Tuple[T, U]) -> U:
    return pair[1]


@pytest.fixture()
def product_fixture() -> Tuple[T, U]:
    return 3, 5


def test_products_functions_first(product_fixture):
    assert product_fixture[0] == first(product_fixture)


def test_products_functions_second(product_fixture):
    assert product_fixture[1] == second(product_fixture)


@pytest.fixture()
def int_bool_fixture() -> Tuple[int, bool]:
    return 2, True


def first_int_bool(pair: Tuple[T, U]) -> T:
    return pair[0]


def second_int_bool(pair: Tuple[T, U]) -> U:
    return pair[1]


mult_common_factor: int = 2


def mult_factor(x: int) -> Tuple[int, bool]:
    return x * mult_common_factor, True


def test_mult_product_first(int_bool_fixture):
    assert first(mult_factor(int_bool_fixture[0])) == int_bool_fixture[0] * 2


def test_mult_product_second(int_bool_fixture):
    assert second(mult_factor(int_bool_fixture[0])) == int_bool_fixture[1]


@pytest.fixture()
def p_q_fixture():
    return 2, False


def test_reconstruct_first_from_int_bool(int_bool_fixture):
    common_factor = mult_factor(int_bool_fixture[0])[0] / int_bool_fixture[0]  # this hurts
    assert common_factor == mult_common_factor


def test_reconstruct_second_from_int_bool(int_bool_fixture):
    assert int_bool_fixture[1] == mult_factor(int_bool_fixture[1])[1]  # somehow this works, true is treated as 1
    # underlying impl?


# problems of factors with different types and a function that discards (more-or-less) the second field.
def test_reconstruct_second_from_p_q(p_q_fixture):
    assert p_q_fixture[1] != mult_factor(p_q_fixture[1])[1]  # somehow this works, true is treated as 1 underlying impl?


if __name__ == '__main__':
    pytest.main()
