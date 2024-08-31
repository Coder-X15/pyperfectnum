#!/usr/bin/env bash

#### IMPORTS ####
import os
import sys
import unittest
import pytest


#### APPENDING PATH ####
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

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

####################### TESTS FOR IS_PERFECT() FUNCTION ################################
def test_is_perfect_positive_int_pass():
    """ 
    Testing the is_perfect() function for positive ints
    """
    assert is_perfect(6) is True
    assert is_perfect(28) is True
    assert not is_perfect(1)
    assert not is_perfect(3)

def test_is_perfect_non_positive_int_pass():
    """ 
    Testing the is_perfect() function for negative ints
    """
    assert not is_perfect(0)
    assert not is_perfect(-2)
    assert not is_perfect(-9)
    assert not is_perfect(-6)
    assert not is_perfect(-28)

def test_is_perfect_positive_float_fail():
    '''
    Testing the is_perfect() function for positive floats
    '''
    with pytest.raises(TypeError):
        is_perfect(1.1)
    with pytest.raises(TypeError):
        is_perfect(19.12)
        
def test_is_perfect_negative_float_fail():
    '''
    Testing the is_perfect() function for negative floats
    '''
    with pytest.raises(TypeError):
        is_perfect(-3.14)
    with pytest.raises(TypeError):
        is_perfect(-6.28)
    
def test_is_perfect_empty_fail():
    '''
    Testing the is_perfect() function for empty args
    '''
    with pytest.raises(TypeError):
        is_perfect()

def test_is_perfect_str_fail():
    """
    Testing the is_perfect() function for string
    """
    with pytest.raises(TypeError):
        is_perfect("1")
    with pytest.raises(TypeError):
        is_perfect("13")

####################### TESTS FOR PERFECT_NUMS_IN_RANGE() FUNCTION ################################
def test_perfect_nums_in_range_positive_int_pass():
    """
    Tests for the  perfect_nums_in_range function for positive ints
    """
    assert perfect_nums_in_range(1) == []
    assert perfect_nums_in_range(5) == []
    assert perfect_nums_in_range(10) == [6]
    assert perfect_nums_in_range(28) == [6, 28]
    assert perfect_nums_in_range(500) == [6, 28, 496]

def test_perfect_nums_in_range_non_positive_int_fail():
    """
    Tests for the  perfect_nums_in_range function for positive ints
    """
    with pytest.raises(ValueError):
        perfect_nums_in_range(0)
    with pytest.raises(ValueError):
        perfect_nums_in_range(-5)
    with pytest.raises(ValueError):
        perfect_nums_in_range(-10)
    with pytest.raises(ValueError):
        perfect_nums_in_range(-2)

def test_perfect_nums_in_range_positive_float_fail():
    """
    Tests for the  perfect_nums_in_range() function for positive ints
    """
    with pytest.raises(TypeError):
        perfect_nums_in_range(1.1)
    with pytest.raises(TypeError):
        perfect_nums_in_range(19.12)

def test_perfect_nums_in_range_negative_float_fail():
    """
    Tests for the  perfect_nums_in_range() function for positive ints
    """
    with pytest.raises(TypeError):
        perfect_nums_in_range(-3.14)
    with pytest.raises(TypeError):
        perfect_nums_in_range(-6.28)
    
def test_perfect_nums_in_range_empty_fail():
    """
    Tests for the  perfect_nums_in_range() function for empty args
    """
    with pytest.raises(TypeError):
        perfect_nums_in_range()


def test_perfect_nums_in_range_str_fail():
    """
    Testing the perfect_nums_in_range() function for strings
    """
    with pytest.raises(TypeError):
        perfect_nums_in_range("1")
    with pytest.raises(TypeError):
        perfect_nums_in_range("13")


if __name__ == "__main__":
    unittest.main(argv=[""], verbosity=2, exit=False)
