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
    def test_either_type(self):
        x = 6
        y = 2
        result: int = divide(x, y)
        self.assertTrue(isinstance(result, Union[str, int]))

    def test_either_second_type(self):
        x = 6
        y = 0
        result: int = divide(x, y)
        self.assertTrue(isinstance(result, Union[str, int]))

    def test_either_invalid(self):
        x = 6
        y = 1
        result: int = divide(x, y)
        self.assertFalse(isinstance(result, Union[str, int]))
if __name__ == '__main__':
    unittest.main()
