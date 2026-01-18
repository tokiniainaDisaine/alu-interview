#!/usr/bin/python3

def minOperations(n):
    if n <= 1:
        return []
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