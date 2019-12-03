from functools import reduce
import math
import operator


def get_sum_of_array(array):
    return reduce((lambda x, y: x + y), array)


def get_max_key_of_dictionary(dictionary):
    return max(dictionary.items(), key=operator.itemgetter(1))[0]


def get_max_value_of_dictionary(dictionary):
    return max(dictionary.values())


def get_matrix(x, y):
    return [[j for j in range(x)] for i in range(y)]


def remove_item_from_list_in_dictionary_value(dictionary, item):
    for k, v in dictionary.items():
        if item in v:
            dictionary[k].remove(item)

    return dictionary

import itertools
# toggle = itertools.cycle(['red', 'green', 'blue']).next
# toggle()

import parse
pr = parse.compile("{} => {}")
# for l in ls:
#     r = pr.parse(l)
#     rules[r[0]] = r[1]

# Functions for 2019
def get_fuel_for_module(module):
    # return (math.floor(module / 3)) - 2
    return module // 3 - 2


def get_fuel_for_fuel(fuel):
    current_fuel = math.floor(fuel / 3) - 2
    if current_fuel < 1:
        return 0
    else:
        return current_fuel + get_fuel_for_fuel(current_fuel)


def map_reduce_fuel(module_list):
    return reduce(operator.add, map(lambda x: x // 3 - 2 if x > 6 else 0, module_list))


def mr_fuel_for_fuel(fuel_list):
    return reduce(operator.add, map(lambda x: get_fuel_for_fuel(x), fuel_list))


def get_intcode(test, i, j):
    test[1] = i
    test[2] = j
    for tranche in [(test[x:x + 4]) for x in range(0, len(test) - 3, 4)]:
        if tranche[0] == 1:
            test[tranche[3]] = test[tranche[1]] + test[tranche[2]]
        if tranche[0] == 2:
            test[tranche[3]] = test[tranche[1]] * test[tranche[2]]
        if tranche[0] == 99:
            return test[0]


def x_y_iter(x, y):
    return itertools.product(range(x), range(y))


def i_j_iter(i, j):
    return itertools.product(range(i), range(j))


def build_wire(wire, direction, amount):
    last_item = wire[-1]
    starting_x = last_item[0]
    starting_y = last_item[1]

    if direction == "R":
        new_items = [[x, starting_y] for x in range(starting_x + 1, starting_x + amount + 1)]
        wire.extend(new_items)
        return wire
    if direction == "L":
        new_items = [[x, starting_y] for x in range(starting_x - 1, starting_x - amount - 1, -1)]
        wire.extend(new_items)
        return wire
    if direction == "U":
        new_items = [[starting_x, y] for y in range(starting_y + 1, starting_y + amount + 1)]
        wire.extend(new_items)
        return wire
    if direction == "D":
        new_items = [[starting_x, y] for y in range(starting_y - 1, starting_y - amount - 1, -1)]
        wire.extend(new_items)
        return wire


def build_intersection_wire(wire, original_wire, direction, amount, intersection):
    starting_x = wire[0]
    starting_y = wire[1]

    if direction == "R":
        new_items = [[x, starting_y] for x in range(starting_x + 1, starting_x + amount + 1)]
        for item in new_items:
            if item in original_wire:
                intersection.append(item)
        return new_items[-1], intersection
    if direction == "L":
        new_items = [[x, starting_y] for x in range(starting_x - 1, starting_x - amount - 1, -1)]
        for item in new_items:
            if item in original_wire:
                intersection.append(item)
        return new_items[-1], intersection
    if direction == "U":
        new_items = [[starting_x, y] for y in range(starting_y + 1, starting_y + amount + 1)]
        for item in new_items:
            if item in original_wire:
                intersection.append(item)
        return new_items[-1], intersection
    if direction == "D":
        new_items = [[starting_x, y] for y in range(starting_y - 1, starting_y - amount - 1, -1)]
        for item in new_items:
            if item in original_wire:
                intersection.append(item)
        return new_items[-1], intersection


def get_manhattan_closest(coord1, coord2):
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])


# Directional Dictionary for Grid Movements
# DX = dict(zip('LRUD', [-1, 1, 0, 0]))
# DY = dict(zip('LRUD', [0, 0, 1, -1]))
# for _ in range(n):
#     x += DX[d]
#     y += DY[d]

