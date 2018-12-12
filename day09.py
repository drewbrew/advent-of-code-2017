#!/usr/bin/env python

"""{}, score of 1.
{{{}}}, score of 1 + 2 + 3 = 6.
{{},{}}, score of 1 + 2 + 2 = 5.
{{{},{},{{}}}}, score of 1 + 2 + 3 + 3 + 3 + 4 = 16.
{<a>,<a>,<a>,<a>}, score of 1.
{{<ab>},{<ab>},{<ab>},{<ab>}}, score of 1 + 2 + 2 + 2 + 2 = 9.
{{<!!>},{<!!>},{<!!>},{<!!>}}, score of 1 + 2 + 2 + 2 + 2 = 9.
{{<a!>},{<a!>},{<a!>},{<ab>}}, score of 1 + 2 = 3.
"""

TEST_INPUTS = {
    '{}': 1,
    "{{{}}}": 6,
    '{{},{}}': 5,
    '{{{},{},{{}}}}': 16,
    '{<a>,<a>,<a>,<a>}': 1,
    '{{<ab>},{<ab>},{<ab>},{<ab>}}': 9,
    '{{<!!>},{<!!>},{<!!>},{<!!>}}': 9,
    '{{<a!>},{<a!>},{<a!>},{<ab>}}': 3,
}

REAL_INPUT = """<paste inputs here>"""


def stream_score(stream):
    in_garbage = False
    in_cleanup = False
    depth = 0
    score = 0
    garbage_chars = 0
    for char in stream:
        if in_garbage:
            if in_cleanup:
                # next char gets skipped
                in_cleanup = False
                continue
            if char == '!':
                in_cleanup = True
                continue
            if char == '>':
                in_garbage = False
                continue
            garbage_chars += 1
        # not in garbage
        else:
            if char == '}':
                # close node
                score += depth
                depth -= 1
                in_garbage = False
                in_cleanup = False
                continue
            if char == '<':
                in_garbage = True
                continue
            if char == '{':
                # open a node
                depth += 1
                continue
            if char == ',':
                # don't care
                continue
            raise ValueError(f'Unexpected character {char}')

    assert depth == 0
    return score, garbage_chars


if __name__ == '__main__':
    for input_string, score in TEST_INPUTS.items():
        test_score, dummy = stream_score(input_string)
        assert test_score == score, (test_score, score, input_string)
    part_one, part_two = stream_score(REAL_INPUT)
    print(part_one, part_two)
