import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
# tests for calculator

import unittest
import pytest


from src.main import isPerfect, perfect_nums_in_range


class TestPerfectNum(unittest.TestCase):

    def test_isPerfect(self):
        self.assertEqual(isPerfect(6), True)
        self.assertEqual(isPerfect(28), True)

    def test_perfect_nums_in_range(self):
        self.assertEqual(perfect_nums_in_range(5), [])
        self.assertEqual(perfect_nums_in_range(9), [6])
        self.assertEqual(perfect_nums_in_range(30), [6, 28])


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
    with pytest.raises(TypeError):
        isPerfect(1.1)
    with pytest.raises(TypeError):
        isPerfect(19.12)
    # test empty arguments
    with pytest.raises(TypeError):
        isPerfect()


def test_isPerfect_str_fail():
    with pytest.raises(TypeError):
        isPerfect("1")
    with pytest.raises(TypeError):
        isPerfect("13")


def test_perfect_nums_in_range():
    assert perfect_nums_in_range(1) == []
    assert perfect_nums_in_range(5) == []
    assert perfect_nums_in_range(10) == [6]
    assert perfect_nums_in_range(14) == [6]
    assert perfect_nums_in_range(27) == [6]
    assert perfect_nums_in_range(28) == [6, 28]
    assert perfect_nums_in_range(30) == [6, 28]
    assert perfect_nums_in_range(500) == [6, 28, 496]

    # test negative numbers
    with pytest.raises(ValueError):
        perfect_nums_in_range(-5)
    with pytest.raises(ValueError):
        perfect_nums_in_range(-10)
    with pytest.raises(ValueError):
        perfect_nums_in_range(-2)
    # test float numbers
    with pytest.raises(TypeError):
        perfect_nums_in_range(1.1)
    with pytest.raises(TypeError):
        perfect_nums_in_range(19.12)
    # test empty arguments
    with pytest.raises(TypeError):
        perfect_nums_in_range()


def test_perfect_nums_in_range_str_fail():
    with pytest.raises(TypeError):
        perfect_nums_in_range("1")
    with pytest.raises(TypeError):
        perfect_nums_in_range("13")


if __name__ == "__main__":
    unittest.main(argv=[""], verbosity=2, exit=False)
