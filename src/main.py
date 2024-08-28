#!/usr/bin/env bash

## EDIT : I just removed an unnecessary import
def is_perfect(n: int) -> bool:
    """
    Returns true if n is a perfect number
    """
    try:
        if n < 0:
            return False
        proper_divisors = [i for i in range(1, n) if n % i == 0]
        return True if sum(proper_divisors) == n else False
    except TypeError:
        raise TypeError(f"Wrong argument type for testing perfectness:{type(n)}")


def perfect_nums_in_range(n: int) -> list:
    """
    Returns  a list of perfect numbers in the range [1, n]
    """
    try:
        if n < 0:
            raise ValueError("Input should be a non-negative integer.")
        return [i for i in range(1, n + 1) if is_perfect(i)]
    except TypeError:
        raise TypeError(f"Wrong argument type for function:{type(n)}")
