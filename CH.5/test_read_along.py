import pytest
from typing import Tuple, TypeVar, Union

T = TypeVar('T')
U = TypeVar('U')


def first(pair: Tuple[T, U]) -> Union[T, U]:
    return pair[0]


def second(pair: Tuple[T, U]) -> Union[T, U]:
    return pair[1]


@pytest.fixture()
def product_fixture() -> Tuple[T, U]:
    return 3, 5


def test_products_functions_first(product_fixture):
    assert product_fixture[0] == first(product_fixture)


def test_products_functions_second(product_fixture):
    assert product_fixture[1] == second(product_fixture)


if __name__ == '__main__':
    pytest.main()
