#!/usr/bin/env python

from collections import deque

TEST_INPUT = 3

REAL_INPUT = 371


def do_spinlock(first_input, iterations=2017):
    spinlock = deque([0])
    for i in range(1, iterations + 1):
        spinlock.rotate(-first_input)
        spinlock.append(i)
    return spinlock


print(do_spinlock(TEST_INPUT)[0])
print(do_spinlock(REAL_INPUT)[0])
part_two = do_spinlock(REAL_INPUT, iterations=50000000)
print(part_two[part_two.index(0) + 1])
