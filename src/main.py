#!/usr/bin/env bash

import math

def isPerfect(n : int) -> bool:
    try:
        proper_divisors = [i for i in range(1, n) if n % i == 0]
        return True if sum(proper_divisors) == n else False
    except TypeError:
        raise TypeError(f"Wrong argument type for testing perfectness:{type(n)}")

def perfect_nums_in_range(n : int) -> list:
    try:
        return [i for i in range(1, n+1) if isPerfect(i)]
    except TypeError:
        raise TypeError(f"Wrong argument type for function:{type(n)}")
