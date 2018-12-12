#!/usr/bin/env python
from functools import reduce
from collections import deque
from operator import xor

RAW_INPUT = "147,37,249,1,31,2,226,0,161,71,254,243,183,255,30,70"
REAL_INPUT = [
    int(i) for i in
    "<paste inputs here>".split(',')
]


def advance_puzzle(
        input_list, puzzle_length=256, skip_size=0, current_position=0,
        start=None):
    start = start or list(range(puzzle_length))
    puzzle = start[:]
    for length in input_list:
        if current_position + length in range(puzzle_length):
            start, stop = list(sorted(
                [current_position, current_position + length]))
            chars_to_reverse = list(reversed(puzzle[start:stop]))
            puzzle[start:stop] = chars_to_reverse[:]
        else:
            stop, start = list(sorted(
                i % puzzle_length for i in
                [current_position, current_position + length]))
            digits_to_reverse = puzzle[start:] + puzzle[:stop]
            for index, char in enumerate(reversed(digits_to_reverse)):
                puzzle[(current_position + index) % puzzle_length] = char
        current_position += length + skip_size
        current_position %= puzzle_length
        skip_size += 1
    return puzzle, current_position, skip_size


def generate_part_two_input(raw_input):
    part_two_string = raw_input.encode('utf-8')
    part_two_input = [i for i in part_two_string] + [17, 31, 73, 47, 23]
    return part_two_input


def generate_checksums(lengths, current_position=0, skip_size=0):
    intermediate = list(range(256))
    for round in range(64):
        intermediate, current_position, skip_size = advance_puzzle(
            lengths, skip_size=skip_size,
            current_position=current_position, start=intermediate,
        )
    checksums = []
    for offset in range(0, 256, 16):
        checksums.append(reduce(xor, intermediate[offset:offset + 16]))
    return checksums


def format_checksums(checksums):
    return ''.join(
        f'{i:02x}' for i in checksums
    )


if __name__ == '__main__':
    test_result = advance_puzzle([3, 4, 1, 5], 5)[0]
    assert test_result == [3, 4, 2, 1, 0], test_result
    part_one, position, skip_size = advance_puzzle(REAL_INPUT)
    print(part_one[0] * part_one[1])
    empty_test = format_checksums(generate_checksums(
        generate_part_two_input('')))
    one_two_three_test = format_checksums(generate_checksums(
        generate_part_two_input('1,2,3')
    ))
    one_two_three_input = generate_part_two_input('1,2,3')
    assert one_two_three_input == [
        int(i) for i in '49,44,50,44,51,17,31,73,47,23'.split(',')
    ], one_two_three_input
    assert empty_test == 'a2582a3a0e66e6e86e3812dcb672a272', empty_test
    print(generate_part_two_input('1,2,3'))
    assert one_two_three_test == '3efbe78a8d82f29979031a4aa0b16a9d', \
        one_two_three_test
    part_two_input = generate_part_two_input(RAW_INPUT)
    checksums = generate_checksums(part_two_input)
    print(format_checksums(checksums))
