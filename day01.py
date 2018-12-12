#!/usr/bin/env python

TEST_INPUTS = {
    '1122': 3,
    '1111': 4,
    '1234': 0,
    '91212129': 9,
}
PART_TWO_TEST_INPUTS = {
    '1212': 6,
    '1221': 0,
    '123425': 4,
    '123123': 12,
    '12131415': 4,
}
REAL_INPUT = '<paste input here>'


def checksum(input_str, offset=1):
    """Sum of all digits which match the next digit"""
    length = len(input_str)
    return sum(
        int(i) for index, i in enumerate(input_str)
        if input_str[(index + offset) % length] == i
    )


if __name__ == '__main__':
    for source, result in TEST_INPUTS.items():
        cs = checksum(source)
        assert cs == result, (source, cs)
    print(checksum(REAL_INPUT))
    for source, result in PART_TWO_TEST_INPUTS.items():
        cs = checksum(source, int(len(source) / 2))
        assert cs == result, (source, cs)
    print(checksum(REAL_INPUT, int(len(REAL_INPUT) / 2)))
