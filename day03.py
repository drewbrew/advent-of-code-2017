#!/usr/bin/env python
from math import sqrt, ceil
from itertools import count

REAL_INPUT = 0


def square_dims(value):
    next_square = ceil(sqrt(value))
    if next_square % 2 == 0:
        # must get an odd value
        next_square += 1
    return next_square


def build_array(puzzle_input):
    array_dimensions = square_dims(puzzle_input)
    grid = [[0] * array_dimensions for i in range(array_dimensions)]
    values = [i for i in range(array_dimensions ** 2 + 1)]
    # now fill the bottom
    for x in range(array_dimensions - 1, 0, -1):
        if x == 0:
            break
        grid[-1][x] = values.pop()
    # then left
    for y in range(array_dimensions - 1, 0, -1):
        if y == 0:
            break
        grid[y][0] = values.pop()
    # then top
    for x in range(array_dimensions - 1):
        grid[0][x] = values.pop()
    # last, right
    for y in range(array_dimensions):
        grid[y][-1] = values.pop()
    return grid


def location_in_grid(grid, puzzle_input):
    array_dimensions = len(grid)
    position = [
        (row.index(puzzle_input), y)
        for y, row in enumerate(grid)
        if puzzle_input in row
    ][0]
    return abs(position[0] - int(array_dimensions / 2)) + abs(
        position[1] - int(array_dimensions / 2)
    )


def sum_spiral():
    # heavily influenced by the reddit spoilers thread; I wouldn't have thought
    # of using count() otherwise
    coords = {(0, 0): 1}
    x = 0
    y = 0
    for i in count(1, 2):
        for (di, dx, dy) in [
            (0, 1, 0), (0, 0, -1), (1, -1, 0), (1, 0, 1),
        ]:
            for dummy in range(i + di):
                x += dx
                y += dy
                coords[(x, y)] = sum(
                    coords.get((k, l), 0)
                    for k in range(x - 1, x + 2)
                    for l in range(y - 1, y + 2)
                )
                yield coords[x, y]


if __name__ == '__main__':
    print(location_in_grid(build_array(REAL_INPUT), REAL_INPUT))
    for val in sum_spiral():
        if val > REAL_INPUT:
            print(val)
            break
