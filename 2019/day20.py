from collections import deque

import networkx as nx
import day20_input as d20

from aocd.models import Puzzle

puzzle = Puzzle(year=2019, day=20)

# map_lines = d20.test.splitlines()
map_lines = puzzle.input_data.splitlines()

master = {}
for y, line in enumerate(map_lines):
    for x, char in enumerate(list(line)):
        coord = complex(x, y)
        if char == " ": continue
        if char in master:
            master[char].append(coord)
        else:
            master[char] = [coord]
        master[coord] = char

portals_name = {}
portals_coord = {}
orthogonal = [complex(0 - 1j), complex(0 + 1j), complex(-1 + 0j), complex(1 + 0j)]
for dot in master["."]:
    for move in orthogonal:
        if master[dot + move][0].isupper():
            if move.real == -1 or move.imag == -1:
                name = "".join([master[dot + move + move][0], master[dot + move][0]])
            else:
                name = "".join([master[dot + move][0], master[dot + move + move][0]])
            if name in portals_name:
                portals_name[name].append(dot)
            else:
                portals_name[name] = [dot]

            portals_coord[dot] = name






def get_steps(start):
    current = start[1:]
    value_map = {current: 0}
    explored = deque([current])
    steps = -1

    def get_options(pos):
        for option in orthogonal:
            coord = pos + option
            if coord in master["."]:
                yield coord

    while explored:
        steps += 1
        for i in range(len(explored)):
            pos = explored.popleft()
            value_map[pos] = steps
            for path in get_options(pos):
                if path not in value_map:
                    if path in portals_coord:
                        yield (portals_coord[path], path, steps + 1)

                    explored.append(path)


def create_directed_graph():
    G = nx.MultiDiGraph()
    starting = "AA"
    starting_coord = portals_name[starting][0]

    def add_edges_to_graph(starting, start_steps):
        starting_name = portals_coord[starting]

        if starting_name == "1ZZ" or starting_name == "1AA" and start_steps != 0:
            return

        for end_name, end_coord, steps in get_steps(starting):
            if starting_name in G.nodes:
                if end_name in G.successors(starting_name): continue
            for option in portals_name[end_name]:
                if end_name == "ZZ" or option != end_coord:
                    starting = option
            G.add_edge(starting_name, end_name, steps=(steps))
            add_edges_to_graph(starting, start_steps + 1)

    add_edges_to_graph(starting_coord, 0)
    # These aren't right for some reason??
    path = nx.shortest_path(G, "1AA", "11ZZ")
    print(path)
    portal_steps = len(path) - 2
    print(nx.shortest_path_length(G, "AA", "1ZZ", "steps"))


def create_directed_graph():
    G = nx.MultiDiGraph()
    starting = "1AA"
    starting_coord = portals_name[starting][0]

    def add_edges_to_graph(starting, start_steps):
        starting_name = portals_coord[starting]

        if starting_name == "ZZ" or starting_name == "AA" and start_steps != 0:
            return

        for end_name, end_coord, steps in get_steps(starting):
            if starting_name in G.nodes:
                if end_name in G.successors(starting_name): continue
            for option in portals_name[end_name]:
                if end_name == "ZZ" or option != end_coord:
                    starting = option
            G.add_edge(starting_name, end_name, steps=(steps))
            add_edges_to_graph(starting, start_steps + 1)

    add_edges_to_graph(starting_coord, 0)
    # These aren't right for some reason??
    path = nx.shortest_path(G, "AA", "ZZ")
    print(path)
    portal_steps = len(path) - 2
    print(nx.shortest_path_length(G, "AA", "ZZ", "steps") + portal_steps)


create_directed_graph()
create_leveled_graph()
