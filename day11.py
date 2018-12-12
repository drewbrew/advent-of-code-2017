#!/usr/bin/env python

TEST_INPUTS = {
    'ne,ne,ne': 3,
    'ne,ne,sw,sw': 0,
    'ne,ne,s,s': 2,
    'se,sw,se,sw,sw': 3,
}

REAL_INPUT = """<paste inputs here>"""


def distance_away(steps):
    x = 0
    y = 0
    z = 0
    max_dist = 0
    # wait, z?!?
    # https://www.redblobgames.com/grids/hexagons/
    offsets = {
        'n': (0, 1, -1),
        'ne': (1, 0, -1),
        'nw': (-1, 1, 0),
        'sw': (-1, 0, 1),
        's': (0, -1, 1),
        'se': (1, -1, 0),
    }
    for step in steps.split(','):
        dx, dy, dz = offsets[step]
        x += dx
        y += dy
        z += dz
        dist = int((abs(x) + abs(y) + abs(z)) / 2)
        if dist > max_dist:
            max_dist = dist
    return int((abs(x) + abs(y) + abs(z)) / 2), max_dist


for steps, dist in TEST_INPUTS.items():
    dist_away, dummy = distance_away(steps)
    assert dist == dist_away, (steps, dist, dist_away)
print(distance_away(REAL_INPUT))
