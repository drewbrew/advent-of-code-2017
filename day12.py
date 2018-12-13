#!/usr/bin/env python

from networkx import Graph, node_connected_component, \
    number_connected_components


TEST_INPUT = """0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5""".split('\n')


REAL_INPUT = """<paste inputs here>""".split('\n')


def build_graph(input_list):
    graph = Graph()
    for line in input_list:
        prog, neighbors = line.split(' <-> ')
        graph.add_edges_from(
            (prog, neighbor) for neighbor in neighbors.split(', '))
    return graph


def part_one(input_list):
    graph = build_graph(input_list)
    return len(node_connected_component(graph, '0'))


if __name__ == '__main__':
    test_part_one = part_one(TEST_INPUT)
    assert test_part_one == 6
    print('Day 11, part 1 solution', part_one(REAL_INPUT))
    print('Day 11, part 2 solution', number_connected_components(
        build_graph(REAL_INPUT)))
