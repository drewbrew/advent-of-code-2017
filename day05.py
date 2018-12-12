#!/usr/bin/env python

from collections import deque

TEST_INPUT = """0
3
0
1
-3""".split('\n')

REAL_INPUT = """<paste inputs here>""".split('\n')

TEST_JUMPS = deque(int(i) for i in TEST_INPUT)
REAL_JUMPS = deque(int(i) for i in REAL_INPUT)

def jump(jump_deque, last_offset, part_two=False):
    jump_value = jump_deque[0]
    if part_two:
        if jump_value < 3:
            jump_deque[0] += 1
        else:
            jump_deque[0] -= 1
    else:
        jump_deque[0] += 1
    if last_offset + jump_value not in range(len(jump_deque)):
        return None
    # need to rotate in the opposite direction
    jump_deque.rotate(0 - jump_value)
    return last_offset + jump_value


def run_puzzle(jump_deque, part_two=False):
    last_offset = 0
    turns = 0
    while last_offset is not None:
        last_offset = jump(jump_deque, last_offset, part_two)
        turns += 1
    return turns


if __name__ == '__main__':
    turns = run_puzzle(TEST_JUMPS.copy())
    assert turns == 5, turns
    assert list(TEST_JUMPS) == [0, 3, 0, 1, -3], TEST_JUMPS
    print(run_puzzle(REAL_JUMPS.copy()))
    turns = run_puzzle(TEST_JUMPS, True)
    assert turns == 10, turns
    print(run_puzzle(REAL_JUMPS, True))
