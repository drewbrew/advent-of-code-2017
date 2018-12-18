#!/usr/bin/env python
from collections import deque

TEST_INPUT = "s1,x3/4,pe/b".split(',')

REAL_INPUT = """<paste inputs here>""".split(',')


def do_step(current_order, step):
    if step[0] == 's':
        interim = deque(current_order)
        interim.rotate(int(step[1:]))
        result = list(interim)
    elif step[0] == 'x':
        before, after = [int(i) for i in step[1:].split('/')]
        result = current_order[:]
        temp = result[after]
        result[after] = result[before]
        result[before] = temp
    elif step[0] == 'p':
        result = current_order[:]
        before, after = [i for i in step[1:].split('/')]
        before_index = result.index(before)
        after_index = result.index(after)
        temp = result[after_index]
        result[after_index] = result[before_index]
        result[before_index] = temp
    else:
        raise ValueError(f'unknown step {step}')
    return result


def do_dance(steps, starting_position='abcdefghijklmnop', dances=1):
    order = [i for i in starting_position]
    dance = 0
    seen = []
    while dance < dances:
        if order in seen:
            print(f'Found loop after {dance} dances')
            return "".join(seen[dances % dance])
        seen.append(order)
        for step in steps:
            order = do_step(order, step)
        dance += 1
        if not dance % 1000:
            print(dance, ''.join(order))
    return ''.join(order)


if __name__ == '__main__':
    test_result = do_dance(TEST_INPUT, 'abcde')
    assert test_result == 'baedc', test_result
    print('tests passed')
    print(do_dance(REAL_INPUT))
    print(do_dance(REAL_INPUT, dances=int(1e9)))
