"""Day 22: virus alert"""
import enum
from typing import List, Dict, Tuple, Union
from collections import defaultdict

TEST_INPUT = """..#
#..
...""".splitlines()

REAL_INPUT = """...#.##.#.#.#.#..##.###.#
......##.....#####..#.#.#
#..####.######.#.#.##...#
...##..####........#.#.#.
.#.#####..#.....#######..
.#...#.#.##.#.#.....#....
.#.#.#.#.#####.#.#..#...#
###..##.###.#.....#...#.#
#####..#.....###.....####
#.##............###.#.###
#...###.....#.#.##.#..#.#
.#.###.##..#####.....####
.#...#..#..###.##..#....#
##.##...###....##.###.##.
#.##.###.#.#........#.#..
##......#..###.#######.##
.#####.##..#..#....##.##.
###..#...#..#.##..#.....#
##..#.###.###.#...##...#.
##..##..##.###..#.##..#..
...#.#.###..#....##.##.#.
##.##..####..##.##.##.##.
#...####.######.#...##...
.###..##.##..##.####....#
#.##....#.#.#..#.###..##.""".splitlines()


class NodeState(enum.Enum):
    CLEAN = 0
    WEAKENED = 1
    INFECTED = 2
    FLAGGED = 3


NEXT_HEADINGS = {
    NodeState.CLEAN: 1j,
    NodeState.WEAKENED: 1,
    NodeState.INFECTED: -1j,
    NodeState.FLAGGED: -1,
}


def parse_grid(
    grid: List[str], part_two: bool = False
) -> Tuple[complex, Dict[complex, Union[NodeState, bool]]]:
    result = defaultdict(lambda: False if not part_two else NodeState.CLEAN)
    assert len(grid) == len(grid[0])
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if part_two:
                result[x - (1j * y)] = (
                    NodeState.INFECTED if char == "#" else NodeState.CLEAN
                )
            else:
                result[x - (1j * y)] = char == "#"
    center = (len(grid[0]) // 2) - 1j * (len(grid) // 2)
    return center, result


def take_turn_part_two(
    grid: Dict[complex, Union[NodeState, bool]], pos: complex, heading: complex
) -> Tuple[Dict[complex, bool], complex, complex, bool]:
    next_state = {
        NodeState.CLEAN: NodeState.WEAKENED,
        NodeState.WEAKENED: NodeState.INFECTED,
        NodeState.INFECTED: NodeState.FLAGGED,
        NodeState.FLAGGED: NodeState.CLEAN,
    }[grid[pos]]
    heading *= NEXT_HEADINGS[grid[pos]]
    grid[pos] = next_state
    pos += heading
    infection_caused = next_state == NodeState.INFECTED
    return grid, pos, heading, infection_caused


def take_turn(
    grid: Dict[complex, Union[NodeState, bool]], pos: complex, heading: complex
) -> Tuple[Dict[complex, bool], complex, complex, bool]:
    infection_caused = not grid[pos]
    if grid[pos]:
        grid[pos] = False
        heading *= -1j
        pos += heading
    else:
        grid[pos] = True
        heading *= 1j
        pos += heading
    return grid, pos, heading, infection_caused


def part_one(puzzle_input: List[str], turns=1000) -> int:
    pos, grid = parse_grid(puzzle_input)
    heading = 1j
    infections_caused = 0
    for _ in range(turns):
        grid, pos, heading, infection_caused = take_turn(grid, pos, heading)
        infections_caused += infection_caused

    return infections_caused


def part_two(puzzle_input: List[str], turns=10000000) -> int:
    pos, grid = parse_grid(puzzle_input, part_two=True)

    heading = 1j
    infections_caused = 0
    for _ in range(turns):
        grid, pos, heading, infection_caused = take_turn_part_two(grid, pos, heading)
        infections_caused += infection_caused
    return infections_caused


assert part_one(TEST_INPUT, 7) == 5
assert part_one(TEST_INPUT, 70) == 41
assert part_one(TEST_INPUT, 10000) == 5587
print(part_one(REAL_INPUT, 10000))
assert part_two(TEST_INPUT, 7) == 1
assert part_two(TEST_INPUT, 100) == 26
print(part_two(REAL_INPUT, 10000000))
