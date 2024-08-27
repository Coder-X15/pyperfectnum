import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# tests for calculator

import unittest
import pytest


from src.main import isPerfect, perfect_nums_in_range

class TestPerfectNum(unittest.TestCase):

    def test_isPerfect(self):
        self.assertEqual(isPerfect(6), True)
        self.assertEqual(isPerfect(28), True)

def test_isPerfect():
    assert isPerfect(6) == True
    assert isPerfect(28) == True
    assert isPerfect(1) == False
    assert isPerfect(3) == False
    # test negative numbers
    assert isPerfect(-2) == False
    assert isPerfect(-9) == False
    assert isPerfect(-6) == False
    assert isPerfect(-28) == False
    # test float numbers
    assert isPerfect(1.1) == False
    assert isPerfect(19.12) == False
    # test empty arguments
    assert isPerfect() == False


def test_addition_str_fail():
    with pytest.raises(TypeError):
        isPerfect("1")
    with pytest.raises(TypeError):
        isPerfect("13")


if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)