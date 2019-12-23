from collections import deque
from itertools import takewhile, combinations_with_replacement, combinations, permutations
import time
import string
import copy
import networkx as nx

start_time = time.time()
# from aocd.models import Puzzle
#
# puzzle = Puzzle(year=2019, day=18)

test = """########################
#f.D.E.e.C.b.A.@.a.B.c.#
######################.#
#d.....................#
########################"""

test2 = """########################
#f.D.E.e.C.b.A.@.a.B.c.#
########################"""

test3 = """#################
#i.G..c...e..H.p#
########.########
#j.A..b...f..D.o#
########@########
#k.E..a...g..B.n#
########.########
#l.F..d...h..C.m#
#################"""

test4 = """########################
#@..............ac.GI.b#
###d#e#f################
###A#B#C################
###g#h#i################
########################"""

test5 = """########################
#...............b.C.D.f#
#.######################
#.....@.a.B.c.d.A.e.F.g#
########################"""

movement = {
    "north": 0 + 1j,
    "south": 0 - 1j,
    "east": 1 + 0j,
    "west": -1 + 0j
}

map_lines = test3.splitlines()
# map_lines = puzzle.input_data.splitlines()

master = {}
for y, line in enumerate(map_lines):
    for x, char in enumerate(list(line)):
        if char in master:
            master[char].append(complex(x, y))
        else:
            master[char] = [complex(x, y)]


legend = {}
pathing = []
all_keys = sorted([x for x in master.keys() if x.islower()])
lower_letter_legend = {}
lower_coord_legend = {}
lower_at_legend = {}
upper_coord_legend = {}
for symbol, coords in master.items():
    if symbol not in ["#", "."]:
        for coord in coords:
            legend[coord] = symbol

    if symbol not in ["#"]:
        for coord in coords:
            pathing.append(coord)

    if symbol in list(string.ascii_lowercase):
        lower_coord_legend[coords[0]] = symbol
        lower_letter_legend[symbol] = coords[0]

    if symbol in list(string.ascii_lowercase) or symbol == "@":
        lower_at_legend[coords[0]] = symbol

    if symbol in list(string.ascii_uppercase):
        upper_coord_legend[coords[0]] = symbol
        upper_coord_legend[symbol] = coords[0]


def get_options(pos):
    options = []
    for k, v in movement.items():
        new = pos + v
        if new in pathing:
            options.append(new)
    return options


def get_step_by_step(coord1, coord2, path):
    path.append(coord1)
    if coord1 == coord2:
        return True, path

    finished = False
    options = [x for x in get_options(coord1) if x not in path]
    if options:
        for option in options:
            if finished or coord1 == coord2:
                return True, path
            finished, path = get_step_by_step(option, coord2, path)
        else:
            if finished:
                return True, path
            else:
                return False, path[:-1]
    else:
        return False, path[:-1]


def get_inbetween(coord1, coord2):
    in_between = []
    truth, steps = get_step_by_step(coord1, coord2, [])
    for step in steps[1:-1]:
        if step in lower_coord_legend:
            in_between.append((lower_coord_legend[step], step))
    return in_between


def get_doors(coord1, coord2):
    in_between = []
    truth, steps = get_step_by_step(coord1, coord2, [])
    for step in steps[1:-1]:
        if step in upper_coord_legend:
            in_between.append((upper_coord_legend[step], step))
    return in_between


value_map_cache = {}


def get_steps_between(coord1, legend):
    cache_name = "{}_{}".format(coord1, "".join([str(x) for x in sorted(legend.values())]))
    if cache_name in value_map_cache:
        print("Hit")
        return value_map_cache[cache_name]
    current = coord1
    value_map = {current: 0}
    letter_map = {}
    explored = deque([current])
    steps = -1

    while explored:
        steps += 1
        for i in range(len(explored)):
            pos = explored.popleft()
            value_map[pos] = steps
            for path in get_options(pos):
                if path not in value_map:
                    if path in legend and legend[path].isupper():
                        continue
                    explored.append(path)

    for location, step in value_map.items():
        if location in legend:
            letter_map[legend[location]] = step

    letter_map.pop("@", None)

    letter_map = sorted(letter_map.items(), key=lambda kv: (kv[1], -ord(kv[0])))
    value_map_cache[cache_name] = letter_map
    return letter_map


def build_length_cache(legend):
    cache = {}

    for item, value in legend.items():
        if value not in cache:
            cache[value] = {}
        for length in get_steps_between(item, legend):
            if length[0] == value:
                continue
            updater = {length[0]: length[1]}
            cache[value].update(updater)

    return cache


def build_door_cache(legend):
    cache = {}

    for item, value in legend.items():
        if not value in cache:
            cache[value] = {}
        for item2, value2 in legend.items():
            if not value2 in cache[value]:
                cache[value][value2] = []
            if item == item2:
                continue

            cache[value][value2] = get_doors(item, item2)

    return cache


def process_doors(door_keys, this_key):
    available = []
    delete = []

    door_keys.append(this_key)

    different = copy.deepcopy(door_cache[this_key])

    for door_key in door_keys:
        for item, values in door_cache[this_key].items():
            for n, door in enumerate(values):
                if door[0] == door_key.upper():
                    different[item].pop(0)

    for item, values in different.items():
        if item != this_key and not values:
            available.append(item)
        else:
            continue

    return sorted(available)


length_cache = build_length_cache(lower_at_legend)
door_cache = build_door_cache(lower_at_legend)


def recursive_stepper():
    start = "@"
    steps = 0
    filler = ""
    current = (start, steps, set([]))
    available_cache = {}
    current_min = {}
    answers = []

    def trail_step(current, current_min={}):
        working_item = current
        start_letter = working_item[0]
        start_door = start_letter.upper()
        local_list = sorted(working_item[2])
        cache_name = "{}_{}".format(start_letter, "".join([str(x) for x in local_list]))
        if cache_name in available_cache:
            available = available_cache[cache_name]
        else:
            available = process_doors(local_list, start_letter)
            available_cache[cache_name] = available

        for processed in working_item[2]:
            if processed in available:
                available.remove(processed)

        if start_letter not in local_list:
            local_list.append(start_letter)

        if len(available) == 0:
            answers.append(working_item[1])

        for option in available:
            steps_to = length_cache[start_letter][option]
            new_steps = steps_to + working_item[1]
            min_name = "{}_{}".format(option, "".join([str(x) for x in local_list]))
            if min_name in current_min:
                if new_steps > current_min[min_name]:
                    continue
                else:
                    trail_step((option, new_steps, local_list), current_min)
                    current_min[min_name] = new_steps
            else:
                trail_step((option, new_steps, local_list), current_min)
                current_min[min_name] = new_steps

    trail_step(current, current_min)

recursive_stepper()

start = "@"
steps = 0
filler = ""
tracker = [("@", 0, [], filler)]
available_cache = {}
current_min = {}
answers = []
while tracker:
    working_item = tracker.pop(0)
    start_letter = working_item[0]
    start_door = start_letter.upper()
    local_list = sorted(working_item[2][:])
    cache_name = "{}_{}".format(start_letter, "".join([str(x) for x in local_list]))
    if cache_name in available_cache:
        available = available_cache[cache_name]
    else:
        available = process_doors(local_list, start_letter)
        available_cache[cache_name] = available

    for processed in working_item[2]:
        if processed in available:
            available.remove(processed)

    if start_letter not in local_list:
        local_list.append(start_letter)

    if len(available) == 0:
        answers.append(working_item[1])

    for option in available:
        steps_to = length_cache[start_letter][option]
        new_steps = steps_to + working_item[1]
        min_name = "{}_{}".format(option, "".join([str(x) for x in local_list]))
        if min_name in current_min:
            if new_steps > current_min[min_name]:
                continue
            else:
                tracker.append((option, new_steps, local_list, ""))
                current_min[min_name] = new_steps
        else:
            tracker.append((option, new_steps, local_list, ""))
            current_min[min_name] = new_steps

    if len(tracker) > 2000000:
        new_tracker = []
        for n, track in enumerate(tracker):
            min_name = "{}_{}".format(track[0], "".join([str(x) for x in track[2]]))
            if min_name in current_min:
                if track[1] > current_min[min_name]:
                    continue
                else:
                    new_tracker.append(track)
                    current_min[min_name] = track[1]
            else:
                current_min[min_name] = track[1]

        tracker = new_tracker
        print(len(tracker))
