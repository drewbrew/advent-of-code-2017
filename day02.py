#!/usr/bin/env python

TEST_INPUT = """5 1 9 5
7 5 3
2 4 6 8""".split('\n')
TEST_INPUT_LIST = []
REAL_INPUT = """<paste inputs here>""".split('\n')
REAL_INPUT_LIST = []

PART_TWO_TEST_INPUT = """5 9 2 8
9 4 7 3
3 8 6 5""".split('\n')
PART_TWO_TEST_INPUT_LIST = []

for line in TEST_INPUT:
    TEST_INPUT_LIST.append([int(i) for i in line.split()])

for line in REAL_INPUT:
    REAL_INPUT_LIST.append([int(i) for i in line.split()])

for line in PART_TWO_TEST_INPUT:
    PART_TWO_TEST_INPUT_LIST.append([int(i) for i in line.split()])

def checksum(input_list):
    return sum(
        max(i) - min(i) for i in input_list
    )


def factors(input_list):
    """Get the only two numbers in each row where one is a factor of the other
    """
    result = []
    for row in input_list:
        for index, i in enumerate(row):
            try:
                match = [j for j in row if i % j == 0 and i != j][0]
            except IndexError:
                continue
            else:
                result.append(int(i / match))
                break
    return sum(result)


if __name__ == '__main__':
    assert checksum(TEST_INPUT_LIST) == 18
    print(checksum(REAL_INPUT_LIST))
    assert factors(PART_TWO_TEST_INPUT_LIST) == 9
    print(factors(REAL_INPUT_LIST))
