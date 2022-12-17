from aocd.models import Puzzle
puzzle = Puzzle(year=2022, day=16)
from itertools import combinations, permutations
import networkx as nx

# Merry Christmas everyone!!!
# Always test with the sample input first!!
sample_input = '''Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II'''


def build_data(question_input):

    valve_list = []
    path_map = {}

    for number, output in enumerate(question_input.splitlines()):
        split_output = output.split(" ")

        # Get the source valve and rate.  Save to the valve list
        source_valve = split_output[1]
        rate_info = split_output[4]

        # Get the rate as an integer
        rate = int(rate_info.split("=")[1][0:-1])

        # Save to the valve list if it has a rate
        if rate or source_valve == 'AA':
            valve_list.append((source_valve, rate))

        # Get the destination valves string
        if "valves" in split_output:
            destination_valves = output.split(" valves ")[1].split(", ")
        else:
            destination_valves = [output.split(" valve ")[1]]

        # Save the options to process for shortest distances
        path_map[source_valve] = destination_valves

    return valve_list, path_map


def build_shortest_distances(valve_list, path_map):
    shortest_distances = {}

    G = nx.Graph()

    for valve in path_map.keys():
        G.add_node(valve)

    for node in path_map.keys():
        for edge in path_map[node]:
            G.add_edge(node, edge)

    for valve_pairs in combinations(valve_list, 2):
        source = valve_pairs[0][0]
        target = valve_pairs[1][0]

        name = "{}_{}".format(source, target)
        reverse_name = "{}_{}".format(target, source)

        shortest_path = nx.shortest_path(G, source, target)

        shortest_distances[name] = len(shortest_path) - 1
        shortest_distances[reverse_name] = len(shortest_path) - 1

    return shortest_distances


def question1():
    question_input = sample_input

    # Build out a list of values with values and a mapping of path possibilities
    valve_list, path_map = build_data(question_input)

    # Use networkx to build a dictionary of shortest distances
    shortest_distances = build_shortest_distances(valve_list, path_map)

    # Start with AA every time
    start = ('AA', 0)

    # Setup the max amount variable
    max_amount = 0

    # This will only work for the sample
    for path_options in permutations(valve_list):
        timer = 30
        amount = 0
        step = start
        for number, next_node in enumerate(path_options):
            name = "{}_{}".format(step[0], next_node[0])
            steps_needed = shortest_distances[name]

            timer -= (steps_needed + 1)

            amount += timer * next_node[1]
            step = next_node

            if number == 3:
                print("amount: {}, average: {}".format(amount, (amount / timer)))

        # print("This path: {}\nTotal released: {}".format(path_options, amount))
        print("final amount: {}".format(amount))
        if amount > max_amount:
            max_amount = amount

    print(max_amount)


def question1_alternate():
    # question_input = sample_input
    question_input = puzzle.input_data

    # Build out a list of values with values and a mapping of path possibilities
    valve_list, path_map = build_data(question_input)

    # Use networkx to build a dictionary of shortest distances
    shortest_distances = build_shortest_distances(valve_list, path_map)

    # Pop off the starting block
    first = ('AA', 0)

    def take_next_step(start, seen, timer, amount, results):
        sorted(seen)
        collection_key = "".join(seen)
        results[collection_key] = max(results.get(collection_key, 0), amount)

        for valve, flow in valve_list:
            if {valve} & seen or start[0] == valve:
                continue
            path_key = "{}_{}".format(start[0], valve)
            new_timer = timer - shortest_distances[path_key] - 1
            if new_timer <= 0:
                continue

            take_next_step((valve, flow), {valve} | seen, new_timer, new_timer * flow + amount, results)

        return results

    totals = take_next_step(first, set([]), 30, 0, {})

    print(max(totals.values()))


def question2():
    # question_input = sample_input
    question_input = puzzle.input_data

    # Build out a list of values with values and a mapping of path possibilities
    valve_list, path_map = build_data(question_input)

    # Use networkx to build a dictionary of shortest distances
    shortest_distances = build_shortest_distances(valve_list, path_map)

    # Pop off the starting block
    first = ('AA', 0)

    def take_next_step(start, seen, timer, amount, results):
        sorted(seen)
        collection_key = "_".join(seen)
        results[collection_key] = max(results.get(collection_key, 0), amount)

        for valve, flow in valve_list:
            if {valve} & seen or start[0] == valve:
                continue
            path_key = "{}_{}".format(start[0], valve)
            new_timer = timer - shortest_distances[path_key] - 1
            if new_timer <= 0:
                continue

            take_next_step((valve, flow), {valve} | seen, new_timer, new_timer * flow + amount, results)

        return results

    totals = take_next_step(first, set([]), 26, 0, {})
    totals.pop('')

    max_amount = 0
    for man, man_values in totals.items():
        man_collection = set(man.split("_"))
        for elephant, elephant_values in totals.items():
            elephant_collection = set(elephant.split("_"))

            if man_collection & elephant_collection:
                continue

            amount = man_values + elephant_values

            if amount > max_amount:
                max_amount = amount

    print(max_amount)


if __name__ == '__main__':
    # question1()
    # question1_alternate()
    question2()

