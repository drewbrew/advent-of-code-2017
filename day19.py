#!/usr/bin/env python

import string

TEST_INPUT = """     |
     |  +--+
     A  |  C
 F---|----E|--+
     |  |  |  D
     +B-+  +--+
""".split('\n')

REAL_INPUT = """<paste inputs here>""".split('\n')  # noqa


def build_puzzle(puzzle_input):
    grid = {}
    for y, row in enumerate(puzzle_input):
        for x, char in enumerate(row):
            if char == ' ':
                continue
            if char in string.ascii_uppercase:
                grid[(x, y)] = char
            else:
                # set grid to True if it's a turn, else False
                grid[(x, y)] = char == '+'
    return grid


def move_through_grid(grid, current_position=None, direction=None):
    if current_position is None:
        top_row_candidates = [
            position for position, value in grid.items()
            if position[1] == 0
        ]
        assert len(top_row_candidates) == 1, top_row_candidates
        current_position = top_row_candidates[0]
        direction = (0, 1)
    chars_seen = []
    turns = 0
    while True:
        try:
            current_value = grid[current_position]
        except KeyError:
            print('Fell off the edge of the world')
            return ''.join(chars_seen), turns
        if grid[current_position] is True:
            # we have a turn
            # search neighbors for a grid spot
            x, y = current_position
            neighbors = [
                (position, value) for position, value in grid.items()
                if position in [
                    (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1),
                ]
            ]
            assert len(neighbors) == 2
            prev_position = (
                current_position[0] - direction[0],
                current_position[1] - direction[1],
            )
            if prev_position not in [i[0] for i in neighbors]:
                raise ValueError(
                    f'No idea where I came from! Position {current_position},'
                    f' Calculated previous {prev_position}, direction '
                    f'{direction}; neighbors {neighbors}')
            new_position = [
                i[0] for i in neighbors if i[0] != prev_position][0]
            direction = (
                new_position[0] - current_position[0],
                new_position[1] - current_position[1],
            )
            current_position = new_position
            turns += 1
            continue
        elif grid[current_position]:
            # we hit a letter
            # mark it and move on
            print(f'hit {grid[current_position]} at {current_position}')
            chars_seen.append(grid[current_position])
        current_position = (
            current_position[0] + direction[0],
            current_position[1] + direction[1],
        )
        turns += 1


def display_grid(grid):
    x_list = sorted(grid, key=lambda k: k[0])
    y_list = sorted(grid, key=lambda k: k[1])
    min_x = x_list[0][0]
    max_x = x_list[-1][0]
    min_y = y_list[0][1]
    max_y = y_list[-1][1]
    for y in range(min_y, max_y + 1):
        row = []
        for x in range(min_x, max_x + 1):
            char = grid.get((x, y), ' ')
            if char is False:
                char = '.'
            elif char is True:
                char = '+'
            row.append(char)
        print(''.join(row))


if __name__ == '__main__':
    test_grid = build_puzzle(TEST_INPUT)
    display_grid(test_grid)
    test_result = move_through_grid(test_grid)
    assert test_result == ('ABCDEF', 38)
    print('tests passed')
    part_one, part_two = move_through_grid(build_puzzle(REAL_INPUT))
    print('Day 19, part 1 solution:', part_one)
    print('Day 19, part 2 solution:', part_two')
