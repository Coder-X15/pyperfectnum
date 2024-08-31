#!/usr/bin/env bash


## EDIT : I just removed an unnecessary import
def is_perfect(n: int) -> bool:
    """
    Args:
        n : a positive integer
    Returns:
        bool: `True` if n is a perfect number (i.e., a number that is equal to the sum of its proper divisors) else `False`
        (NB: The same returns False even when n is less than or equal to 0)
    Raises:
        TypeError: if  n is not an integer
    Examples:
        >>>  is_perfect(6) # 6 is a perfect number
        True
        >>> is_perfect(9) # 9 is not a perfect number
        False
        >>> is_perfect(1.2) # wrong type of argument
        Traceback (most exception):
        ...
        TypeError: Wrong argument type for testing perfectness: <class 'float'>
        >>> is_perfect("10") # wrong type of argument
        Traceback (most exception):
        ...
        TypeError: Wrong argument type for testing perfectness: <class 'str'>
    """
    try:
        if n <= 0 and type(n) == int:
            return False
        proper_divisors = [i for i in range(1, n) if n % i == 0]
        return True if sum(proper_divisors) == n else False
    except TypeError:
        raise TypeError(f"Wrong argument type for testing perfectness:{type(n)}")


def perfect_nums_in_range(n: int) -> list:
    """
    Args:
        n : a positive integer
    Returns:
        list: A list of perfect numbers in the list [i for i in range(1, n+1)]
    Raises:
        TypeError: if  n is not an integer
        ValueError: if n is not a positive integer
    Examples:
        >>>  perfect_nums_in_range(6)
        [6]
        >>> perfect_nums_in_range(9)
        [6]
        >>> perfect_nums_in_range(1.2) # wrong type of argument
        Traceback (most exception):
        ...
        TypeError: Wrong argument type for function: <class 'float'>
        >>> perfect_nums_in_range("12") # wrong type of argument
        Traceback (most exception):
        ...
        TypeError: Wrong argument type for function: <class 'str'>
        >>> perfect_nums_in_range(-8) # wrong kind of argument
        Traceback (most exception):
        ...
        ValueError: Input should be a positive integer
    """
    try:
        if n <= 0 and type(n) == int:
            raise ValueError("Input should be a positive integer.")
        return [i for i in range(1, n + 1) if is_perfect(i)]
    except TypeError:
        raise TypeError(f"Wrong argument type for function:{type(n)}")
