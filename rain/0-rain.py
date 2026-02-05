#!/usr/bin/python3
"""
Docstring for rain.0-rain
"""


def rain(walls):
    """
    Docstring for rain

    :param walls: Description
    """
    if not walls or len(walls) < 3:
        return 0

    rain = 0
    for i in range(1, len(walls) - 1):
        left = max(walls[:i])
        right = max(walls[i + 1:])
        min_wall = min(left, right)
        if walls[i] < min_wall:
            rain += min_wall - walls[i]
    return rain
