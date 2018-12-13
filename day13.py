#!/usr/bin/env python
from itertools import count
from math import ceil

TEST_INPUT = """0: 3
1: 2
4: 4
6: 4""".split('\n')

REAL_INPUT = """<paste inputs here>""".split('\n')

TEST_INPUT_DICT = {
    int(line.split(': ')[0]): int(line.split(': ')[1])
    for line in TEST_INPUT
}


REAL_DICT = {
    int(line.split(': ')[0]): int(line.split(': ')[1])
    for line in REAL_INPUT
}


def scanner(depth, time_index):
    offset = time_index % ((depth - 1) * 2)

    return 2 * (depth - 1) - offset if offset > depth - 1 else offset


def part_one(input_dict):
    # yes, this is heavily stolen from the reddit megathread
    return sum(
        pos * depth
        for pos, depth
        in input_dict.items() if scanner(depth, pos) == 0)


def part_two(input_dict):
    return next(
        wait for wait in count()
        if not any(
            scanner(depth, wait + pos) == 0
            for pos, depth in input_dict.items()
        )
    )


if __name__ == '__main__':
    part_one_score = part_one(TEST_INPUT_DICT)
    assert part_one_score == 24, part_one_score
    print(part_one(REAL_DICT))
    part_two_result = part_two(TEST_INPUT_DICT)
    assert part_two_result == 10, part_two_result
    print(part_two(REAL_DICT))
