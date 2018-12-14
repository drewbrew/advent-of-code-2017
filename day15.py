#!/usr/bin/env python

GEN_A = 16807
GEN_B = 48271

DIVISOR = 2147483647

TEST_STARTS = [65, 8921]
REAL_STARTS = []  # Insert inputs here

TEST_SEQUENCES = {
   (1092455, 430625591): False,
   (1181022009, 1233683848): False,
   (245556042, 1431495498): True,
   (1744312007, 137874439): False,
   (1352636452, 285222916): False,
}


def common_iterations(starting_points, iterations=40000000):
    common = 0
    gen_a, gen_b = starting_points
    for iteration in range(iterations):
        gen_a = (gen_a * GEN_A) % DIVISOR
        gen_b = (gen_b * GEN_B) % DIVISOR
        if gen_a % 65536 == gen_b % 65536:
            common += 1
    return common


def part_two(starting_points, candidates=5000000):
    common = 0
    gen_a, gen_b = starting_points
    a_candidates = []
    b_candidates = []
    while len(a_candidates) < candidates or len(b_candidates) < candidates:
        gen_a = (gen_a * GEN_A) % DIVISOR
        gen_b = (gen_b * GEN_B) % DIVISOR
        if not gen_a % 4:
            a_candidates.append(gen_a)
        if not gen_b % 8:
            b_candidates.append(gen_b)
    if starting_points == TEST_STARTS:
        assert a_candidates[:5] == [
            1352636452, 1992081072, 530830436, 1980017072, 740335192,
        ], a_candidates[:5]
        assert b_candidates[:5] == [
            1233683848, 862516352, 1159784568, 1616057672, 412269392,
        ], b_candidates[:5]
        assert a_candidates[1055] == 1023762912, a_candidates[1055:1058]
        assert b_candidates[1055] == 896885216, b_candidates[1055:1058]
        assert a_candidates[1055] % 65536 == b_candidates[1055] % 65536, \
            (a_candidates[1055] % 65536, b_candidates[1055] % 65536)
    print(f'found {len(a_candidates)} from A, {len(b_candidates)} from B')
    common = 0
    for a, b in zip(a_candidates, b_candidates):
        if (a % 65536) == (b % 65536):
            common += 1
    return common


if __name__ == '__main__':
    test_result = common_iterations(TEST_STARTS, 5)
    assert test_result == 1
    test_part_two = part_two(TEST_STARTS)
    assert test_part_two == 309, test_part_two
    print('tests passed')
    print('Day 15, part 1:', common_iterations(REAL_STARTS))

    print('Day 15, part 2:', part_two(REAL_STARTS))
