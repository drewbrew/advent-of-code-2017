#!/usr/bin/env python

TEST_INPUT = [0, 2, 7, 0]
REAL_INPUT = list(
    int(i) for i in
    '<paste inputs here>'.split())

def redistribute_blocks(block_list):
    new_list = block_list[:]
    index, blocks = sorted(
        enumerate(block_list), key=lambda k: (0 - k[1], k[0]))[0]
    offset = (index + 1) % len(block_list)
    while blocks > 0:
        new_list[index] -= 1
        new_list[offset] += 1
        offset = (offset + 1) % len(block_list)
        blocks -= 1
    return new_list


def part_one(block_list):
    blocks_seen = set()
    blocks_seen.add(tuple(block_list))
    iterations = 0
    last_blocks = block_list[:]
    while True:
        iterations += 1
        last_blocks = redistribute_blocks(last_blocks)
        new_blocks = tuple(last_blocks)
        if new_blocks in blocks_seen:
            return iterations, last_blocks
        blocks_seen.add(new_blocks)


if __name__ == '__main__':
    part_one_result, dummy = part_one(TEST_INPUT)
    assert part_one_result == 5, part_one_result
    iterations, first_duplicate = part_one(REAL_INPUT)
    print('Day 6, part 1 solution', iterations)
    iterations, second_duplicate = part_one(first_duplicate)
    assert first_duplicate == second_duplicate
    print('Day 6, part 2 solution', iterations)
