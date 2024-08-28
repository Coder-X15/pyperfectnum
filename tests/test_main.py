import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
# tests for calculator

import unittest
import pytest


from src.main import is_perfect, perfect_nums_in_range


class TestPerfectNum(unittest.TestCase):
    """
    Class for running tests
    """

    def test_is_perfect(self):
        """
        tests for the  is_perfect function
        """
        self.assertEqual(is_perfect(6), True)
        self.assertEqual(is_perfect(28), True)

    def test_perfect_nums_in_range(self):
        """
        tests for the perfect_nums_in_range function
        """
        self.assertEqual(perfect_nums_in_range(5), [])
        self.assertEqual(perfect_nums_in_range(9), [6])
        self.assertEqual(perfect_nums_in_range(30), [6, 28])


def test_is_perfect():
    """ """
    assert is_perfect(6) is True
    assert is_perfect(28) is True
    assert not is_perfect(1)
    assert not is_perfect(3)
    # test negative numbers
    assert not is_perfect(-2)
    assert not is_perfect(-9)
    assert not is_perfect(-6)
    assert not is_perfect(-28)
    # test float numbers
    with pytest.raises(TypeError):
        is_perfect(1.1)
    with pytest.raises(TypeError):
        is_perfect(19.12)
    # test empty arguments
    with pytest.raises(TypeError):
        is_perfect()


def test_is_perfect_str_fail():
    with pytest.raises(TypeError):
        is_perfect("1")
    with pytest.raises(TypeError):
        is_perfect("13")


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
