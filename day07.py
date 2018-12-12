#!/usr/bin/env python
from collections import Counter

TEST_INPUTS = """pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)""".split('\n')

REAL_INPUTS = """<paste inputs here>""".split('\n')

TEST_INPUT_DICT = {}
REAL_INPUT_DICT = {}

for line in TEST_INPUTS:
    split = line.split(' ', 2)
    deps = ''
    name = ''
    paren_weight = ''
    try:
        name, paren_weight, deps = split
    except ValueError:
        name, paren_weight = split
    weight = int(paren_weight[1:-1])
    prog_deps = list(i.strip() for i in deps[3:].split(',') if i)
    TEST_INPUT_DICT[name] = (weight, prog_deps)


for line in REAL_INPUTS:
    split = line.split(' ', 2)
    deps = ''
    name = ''
    paren_weight = ''
    try:
        name, paren_weight, deps = split
    except ValueError:
        name, paren_weight = split
    weight = int(paren_weight[1:-1])
    prog_deps = list(i.strip() for i in deps[3:].split(',') if i)
    REAL_INPUT_DICT[name] = (weight, prog_deps)


def sort_progs(prog_dict):
    """Sort programs into the form
    {name: (weight, progs_it_depends_on)}
    """
    dep_dict = {name: [] for name in prog_dict}
    for name, (dummy, dependencies) in prog_dict.items():
        for dep in dependencies:
            dep_dict[dep].append(name)
    return dep_dict


def part_one(sorted_dict):
    zero_deps = [key for key, val in sorted_dict.items() if not val]
    assert len(zero_deps) == 1
    return zero_deps[0]


def total_weight(disc_name, input_dict):
    self_weight, deps = input_dict[disc_name]
    if not deps:
        return self_weight
    child_weight = sum(
        total_weight(i, input_dict) for i in deps)
    return child_weight + self_weight


def unbalanced_disc(disc_name, input_dict):
    self_weight, deps = input_dict[disc_name]
    if not deps:
        return None
    disc_weights = {name: total_weight(name, input_dict) for name in deps}
    weight_counts = Counter(disc_weights.values())
    odd_one_out = [key for key, val in weight_counts.items() if val == 1]
    if not odd_one_out:
        # this one must be our culprit because all the kids are balanced!
        return disc_name, 0
    unbalanced = [
        key for key, val in disc_weights.items() if val == odd_one_out[0]][0]
    unbalanced_child, target_weight = unbalanced_disc(unbalanced, input_dict)
    if target_weight:
        # we've already calculated it; pass it up the stack
        return unbalanced_child, target_weight
    # so at this point, we know what our unbalanced child is
    common_weight = [
        key for key, val in weight_counts.items() if val != 1][0]
    weight_diff = common_weight - odd_one_out[0]
    orig_weight = input_dict[unbalanced_child][0]
    return unbalanced_child, orig_weight + weight_diff


if __name__ == '__main__':
    sorted_test = sort_progs(TEST_INPUT_DICT)
    part_one_result = part_one(sorted_test)
    assert part_one_result == 'tknk', (part_one_result, sorted_dict)
    sorted_real = sort_progs(REAL_INPUT_DICT)
    part_one_result = part_one(sorted_real)
    print('Day 7, part 1 solution:', part_one_result)
    test_weight = total_weight('ugml', TEST_INPUT_DICT)
    assert test_weight == 251, test_weight
    unbalanced_test = unbalanced_disc('tknk', TEST_INPUT_DICT)
    assert unbalanced_test == ('ugml', 60), unbalanced_test
    unbalanced, target = unbalanced_disc(part_one_result, REAL_INPUT_DICT)
    print(f'Day 7, part 2 solution: {unbalanced} new weight {target}')
