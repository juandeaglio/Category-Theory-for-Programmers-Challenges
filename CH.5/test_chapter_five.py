import unittest
from typing import Union


def divide(x: int, y: int) -> Union[str, int]:
    if y == 0:
        return "Division by zero error."

    elif y == 1:
        return x / y

    else:
        return x // y

class ChapterFive(unittest.TestCase):
    # Question 1
    def test_product_type(self):
        x = 6
        y = 2
        result: int = divide(x, y)
        self.assertTrue(isinstance(result, Union[str, int]))

    def test_product_second_type(self):
        x = 6
        y = 0
        result: int = divide(x, y)
        self.assertTrue(isinstance(result, Union[str, int]))

    def test_either_invalid(self):
        x = 6
        y = 1
        result: int = divide(x, y)
        self.assertFalse(isinstance(result, Union[str, int]))

    def test_co_product_better_than_injections(self):
        # Injections
        def int_injection(n: int) -> int:
            return n

        def bool_injection(b: bool) -> int:
            return int(b)

        # Maps the following into this an int:
        #   b       n
        #   |       |
        #   |m      |m
        #   Union   Union
        #   |       |
        #   |       |
        #   v       v
        #  bool---->int
        #       c_i (i.e., cast to int)

        # Factorizing function
        def unionizer(e: Union[int, bool]) -> int:
            return int(e)

        value = 5
        self.assertEqual(int_injection(value), unionizer(value))
        value = True
        self.assertEqual(bool_injection(value), unionizer(value))

    def test_co_product_better_than_indirect_injections(self):
        # Injections
        def int_injection(n: int) -> int:
            if n < 0:
                return n
            else:
                return n + 2

        def bool_injection(b: bool) -> int:
            return int(b)

        # Maps the following into this an int:
        #   b       n
        #   |       |
        #   |m      |m
        #   Union   Union
        #   |       |
        #   |       |
        #   v       v
        #  bool---->int
        #       c_i (i.e., cast to int)

        # Factorizing function
        def unionizer(e: Union[int, bool]) -> int:
            if isinstance(e, bool):
                return 0 if e is False else 1
            elif isinstance(e, int):
                if e < 0:
                    return e
                else:
                    return e + 2

        value = 1
        self.assertEqual(int_injection(value), unionizer(value))
        value = -1
        self.assertEqual(int_injection(value), unionizer(value))
        value = True
        self.assertEqual(bool_injection(value), unionizer(value))


if __name__ == '__main__':
    unittest.main()
