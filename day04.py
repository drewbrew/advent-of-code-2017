#!/usr/bin/env python

TEST_INPUTS = """aa bb cc dd ee
aa bb cc dd aa
aa bb cc dd aaa""".split('\n')
REAL_INPUT = """<paste inputs here>""".split('\n')

PART_TWO_TEST_INPUT = """abcde fghij
abcde xyz ecdab
a ab abc abd abf abj
iiii oiii ooii oooi oooo
oiii ioii iioi iiio""".split('\n')


def valid_passphrase_count(input_list):
    valid = 0
    for line in input_list:
        words = line.split()
        if len(set(words)) == len(words):
            valid += 1
    return valid


def part_two(input_list):
    valid = 0
    for line in input_list:
        words = list(sorted(i) for i in line.split())
        if len(set([''.join(i) for i in words])) == len(words):
            valid += 1
    return valid


if __name__ == '__main__':
    assert valid_passphrase_count(TEST_INPUTS) == 2
    print(valid_passphrase_count(REAL_INPUT))
    assert part_two(PART_TWO_TEST_INPUT) == 3
    print(part_two(REAL_INPUT))
