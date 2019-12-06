from functools import reduce
import itertools
import parse
import math
import operator
import re


def get_sum_of_array(array):
    return reduce((lambda x, y: x + y), array)


def get_max_key_of_dictionary(dictionary):
    return max(dictionary.items(), key=operator.itemgetter(1))[0]


def get_max_value_of_dictionary(dictionary):
    return max(dictionary.values())


def get_matrix(x, y):
    return [[(i, j) for j in range(x)] for i in range(y)]


def remove_item_from_list_in_dictionary_value(dictionary, item):
    for k, v in dictionary.items():
        if item in v:
            dictionary[k].remove(item)

    return dictionary


toggle = itertools.cycle(['red', 'green', 'blue'])
next(toggle)


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


def intcode_computer(intcode_list, input):
    counter = 0
    try:
        while True:

            item = intcode_list[counter]

            ones = int(str(item)[-1])
            tens = int(str(item // 10)[-1])
            hundreds = int(str(item // 100)[-1])
            thousands = int(str(item // 1000)[-1])

            if ones == 1:
                if hundreds == 1:
                    param1 = intcode_list[counter + 1]
                else:
                    position = intcode_list[counter + 1]
                    param1 = intcode_list[position]

                if thousands == 1:
                    param2 = intcode_list[counter + 2]
                else:
                    param2 = intcode_list[intcode_list[counter + 2]]

                intcode_list[intcode_list[counter + 3]] = param1 + param2
                counter += 4

            if ones == 2:
                if hundreds == 1:
                    param1 = intcode_list[counter + 1]
                else:
                    param1 = intcode_list[intcode_list[counter + 1]]

                if thousands == 1:
                    param2 = intcode_list[counter + 2]
                else:
                    param2 = intcode_list[intcode_list[counter + 2]]

                intcode_list[intcode_list[counter + 3]] = param1 * param2
                counter += 4

            if ones == 3:
                # if hundreds == 1:
                #     param1 = intcode_list[counter + 1]
                # else:
                #     param1 = intcode_list[intcode_list[counter + 1]]
                param1 = intcode_list[counter + 1]
                intcode_list[param1] = input
                counter += 2

            if ones == 4:
                if hundreds == 1:
                    param1 = intcode_list[counter + 1]
                else:
                    param1 = intcode_list[intcode_list[counter + 1]]

                print(param1)
                counter += 2

            if ones == 5:
                if hundreds == 1:
                    param1 = intcode_list[counter + 1]
                else:
                    param1 = intcode_list[intcode_list[counter + 1]]

                if thousands == 1:
                    param2 = intcode_list[counter + 2]
                else:
                    param2 = intcode_list[intcode_list[counter + 2]]

                if param1 == 0:
                    counter += 3
                else:
                    counter = param2

            if ones == 6:
                if hundreds == 1:
                    param1 = intcode_list[counter + 1]
                else:
                    param1 = intcode_list[intcode_list[counter + 1]]

                if thousands == 1:
                    param2 = intcode_list[counter + 2]
                else:
                    param2 = intcode_list[intcode_list[counter + 2]]

                if param1 != 0:
                    counter += 3
                else:
                    counter = param2

            if ones == 7:
                if hundreds == 1:
                    param1 = intcode_list[counter + 1]
                else:
                    param1 = intcode_list[intcode_list[counter + 1]]

                if thousands == 1:
                    param2 = intcode_list[counter + 2]
                else:
                    param2 = intcode_list[intcode_list[counter + 2]]

                if param1 < param2:
                    intcode_list[intcode_list[counter + 3]] = 1
                else:
                    intcode_list[intcode_list[counter + 3]] = 0

                counter += 4

            if ones == 8:
                if hundreds == 1:
                    param1 = intcode_list[counter + 1]
                else:
                    param1 = intcode_list[intcode_list[counter + 1]]

                if thousands == 1:
                    param2 = intcode_list[counter + 2]
                else:
                    param2 = intcode_list[intcode_list[counter + 2]]

                if param1 == param2:
                    intcode_list[intcode_list[counter + 3]] = 1
                else:
                    intcode_list[intcode_list[counter + 3]] = 0

                counter += 4

            if ones == 9 and tens == 9:
                print("Complete")
                break
    except:
        print(counter)


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


def get_complex_distance(complex1, complex2):
    return int(abs(complex1.real - complex2.real) + abs(complex1.imag - complex2.imag))


def move_complex(direction, complex_number):
    direction_map = {"U": 1j, "D": -1j, "R": 1, "L": -1}
    return complex_number + direction_map[direction]


def min_max(l):
    return min(l), max(l)


def max_minus_min(l):
    return max(l) - min(l)


def list_diff(x):
    return [b-a for a, b in zip(x, x[1:])]


def flatten(l):
    return [i for x in l for i in x]


def lmap(func, *iterables):
    return list(map(func, *iterables))


def ints(s):
    return lmap(int, re.findall(r"-?\d+", s))


def positive_ints(s):
    return lmap(int, re.findall(r"\d+", s))


def floats(s):
    return lmap(float, re.findall(r"-?\d+(?:\.\d+)?", s))


def positive_floats(s):
    return lmap(float, re.findall(r"\d+(?:\.\d+)?", s))


def words(s):
    return re.findall(r"[a-zA-Z]+", s)


def key_values(d):
    return list(d.items())


def every_digit_greater_equal(l):
    current = l[0]
    rest = l[1:]
    for num in rest:
        if num < current:
            return False
        current = num
    return True


def check_list_against_previous(l):
    # return all(c1 <= c2 for c1, c2 in zip(str(num), str(num)[1:]))
    return all(c1 <= c2 for c1, c2 in zip(str(l), str(l)[1:]))


# Directional Dictionary for Grid Movements
# DX = dict(zip('LRUD', [-1, 1, 0, 0]))
# DY = dict(zip('LRUD', [0, 0, 1, -1]))
# for _ in range(n):
#     x += DX[d]
#     y += DY[d]


# complex1 = 0 + 0j
# complex2 = 5 + 4j
#
# print(get_complex_distance(complex1, complex2))
#
# print(move_complex("U", complex1) + move_complex("U", complex1) + move_complex("L", complex1))
# print(move_complex("D", complex1))
# print(move_complex("L", complex1))
# print(move_complex("R", complex1))
