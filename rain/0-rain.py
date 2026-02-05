#!/usr/bin/python3
"""
Docstring for rain.0-rain
"""

def rain(walls):
    """
    Docstring for rain
    
    :param walls: Description
    """
    num_of_walls = []
    num_of_zeros = []

    total_area = 0
    zero_counter = 0

    for wall_height in walls:
        if wall_height != 0:
            num_of_walls.append(wall_height)
            num_of_zeros.append(zero_counter)
            zero_counter = 0
        else:
            zero_counter += 1

    num_of_zeros.pop(0)

    for i in range(len(num_of_walls)):
        j = min(i, (i + 1)) # the highest water elevation
        height = num_of_walls[j]
        length = num_of_zeros[i]

        water_area = height * length
        total_area += water_area

    return total_area
    