#!/usr/bin/env python

from day10 import generate_checksums, format_checksums, generate_part_two_input

TEST_INPUT = 'flqrgnkx'
REAL_INPUT = '<paste input here>'


def part_one(input_string):
    checksum_inputs = [
        f'{input_string}-{i}'
        for i in range(128)
    ]
    score = 0
    rows = []
    for index, round_input_string in enumerate(checksum_inputs):
        checksums = format_checksums(generate_checksums(
            generate_part_two_input(round_input_string)
        ))
        integer_checksum = int(checksums, 16)
        formatted_checksum = '{:0128b}'.format(integer_checksum)
        assert len(formatted_checksum) == 128, len(formatted_checksum)
        if input_string == TEST_INPUT and index < 8:
            test_results = [
                '11010100',
                '01010101',
                '00001010',
                '10101101',
                '01101000',
                '11001001',
                '01000100',
                '11010110',
            ]
            assert formatted_checksum.startswith(test_results[index]), \
                formatted_checksum
        blocks = list(int(i) for i in formatted_checksum)
        score += sum(blocks)
        rows.append(blocks)
    return score, rows


# cribbed straight from the reddit megathread. NO SHAME!
def dfs(i, j, seen, rows):
    if (i, j) in seen:
        return
    if not rows[j][i]:
        return
    seen.add((i, j))
    if i > 0:
        dfs(i - 1, j, seen, rows)
    if j > 0:
        dfs(i, j - 1, seen, rows)
    if i < 127:
        dfs(i + 1, j, seen, rows)
    if j < 127:
        dfs(i, j + 1, seen, rows)


def part_two(rows):
    seen = set()
    count = 0
    for x in range(128):
        for y in range(128):
            if (x, y) in seen:
                continue
            if not rows[y][x]:
                continue
            count += 1
            dfs(x, y, seen, rows)
    return count


if __name__ == '__main__':
    part_one_score, dummy = part_one(TEST_INPUT)
    assert part_one_score == 8108, part_one_score
    part_one_score, rows = part_one(REAL_INPUT)
    print(part_one_score)
    part_two_score = part_two(dummy)
    assert part_two_score == 1242, part_two_score
    print(part_two(rows))
