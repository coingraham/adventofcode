from collections import deque
import networkx as nx
import day20_input as d20

import sys
sys.setrecursionlimit(15000)

# from aocd.models import Puzzle
# puzzle = Puzzle(year=2019, day=20)

# map_lines = d20.test2.splitlines()
map_lines = d20.puzzle_input.splitlines()

map_size_y = len(map_lines)
map_size_x = len(map_lines[0])

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
    current = start
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


def create_leveled_graph():
    G = nx.MultiDiGraph()
    starting = "AA"
    level = 0
    starting_coord = portals_name[starting][0]
    starting_name = "".join([str(level), starting])
    start_check = "".join([str(level), starting, str(starting_coord.real), str(starting_coord.imag)])

    ending = "ZZ"
    ending_coord = portals_name[ending][0]
    ending_level = -1
    end_check = "".join([str(ending_level), ending, str(ending_coord.real), str(ending_coord.imag)])
    finished = False

    def figure_level(coord, level):
        x, y = int(coord.real), int(coord.imag)
        if x == 2 or x == map_size_x - 3:
            return level - 1
        if y == 2 or y == map_size_y - 3:
            return level - 1
        return level + 1

    def add_edges_to_graph(indentification, start_steps, finished=False):
        starting_level_name, starting = indentification
        if starting_level_name == "-1ZZ" or starting_level_name == "0AA" and start_steps != 0:
            finished = True
            return
        if starting_level_name == "0FD":
            print("Found")

        for end_name, end_coord, steps in get_steps(starting):
            if end_name == "AA" or finished:
                continue
            offset = len(starting_level_name) - 2
            level = int(starting_level_name[:offset])
            this_ending_level_name = "".join([str(level), end_name])
            if level == 50:
                return
            if end_name == "ZZ" and level != 0:
                continue
            for option in portals_name[end_name]:
                if end_name == "ZZ":
                    next_end_coord = option
                elif option != end_coord:
                    next_end_coord = option
            start_tracker = "".join([str(level), starting_level_name[offset:], str(starting.real), str(starting.imag)])
            level = figure_level(end_coord, int(level))
            if end_name != "ZZ" and level < 0:
                continue
            next_ending_level_name = "".join([str(level), end_name])
            end_tracker = "".join([str(level), end_name, str(next_end_coord.real), str(next_end_coord.imag)])
            if start_tracker in G.nodes:
                if end_tracker in G.successors(start_tracker):
                    continue
            # G.add_edge(starting_level_name, this_ending_level_name, steps=steps)
            G.add_edge(start_tracker, end_tracker, steps=steps + 1)
            add_edges_to_graph((next_ending_level_name, next_end_coord), start_steps + 1)

    add_edges_to_graph((starting_name, starting_coord), 0)
    # These aren't right for some reason??
    path = nx.shortest_path(G, start_check, end_check)
    print(path)
    portal_steps = len(path) - 2
    print(nx.shortest_path_length(G, start_check, end_check, "steps") - 1)


# create_directed_graph()
create_leveled_graph()
