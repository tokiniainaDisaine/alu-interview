#!/usr/bin/python3
"""
Doc
"""


def minOperations(n):
    """
    Module doc
    :param n:
    :return:
    """
    n = abs(n)
    
    if n <= 1:
        return 0
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)

    total = 0
    for factor in factors:
        total += factor

    return total
