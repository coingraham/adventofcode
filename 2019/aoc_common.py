from functools import reduce
import itertools
import parse
import math
import operator
import re
from PIL import Image
from PIL import ImageOps
import numpy as np


def get_frame(coords):
    np_coords = np.array([(k[0], k[1]) for k in coords.keys()])
    max_x = max(np_coords[:, 0])
    max_y = max(np_coords[:, 1])
    offset_x = np.abs(min(np_coords[:, 0]))
    offset_y = np.abs(min(np_coords[:, 1]))

    return max_x, max_y, offset_x, offset_y


def get_complex_frame(coords):
    np_coords = np.array([(int(k.real), int(k.imag)) for k in coords.keys()])
    max_x = int(max(np_coords[:, 0]))
    max_y = int(max(np_coords[:, 1]))
    offset_x = int(np.abs(min(np_coords[:, 0])))
    offset_y = int(np.abs(min(np_coords[:, 1])))

    return max_x, max_y, offset_x, offset_y


def screen(coord_dictionary):
    max_x, max_y, offset_x, offset_y = get_frame(coord_dictionary)

    background = 0

    red = (255, 0, 0, 0)
    white = (255, 255, 255, 0)
    green = (0, 255, 0, 0)
    blue = (0, 0, 255, 0)

    im = Image.new('RGB', (max_x + offset_x + 1, max_y + offset_y + 1), color=background)

    for k, v in coord_dictionary.items():
        if v == 1:
            im.putpixel((k[0] + offset_x, k[1] + offset_y), red)
        if v == 2:
            im.putpixel((k[0] + offset_x, k[1] + offset_y), white)
        if v == 3:
            im.putpixel((k[0] + offset_x, k[1] + offset_y), green)
        if v == 4:
            im.putpixel((k[0] + offset_x, k[1] + offset_y), blue)

    h, w = im.size

    upsize = 20
    im = im.resize((h * upsize, w * upsize))

    # im.save('blah.png')
    # im = ImageOps.flip(im)
    im.show()


def screen_complex(coord_dictionary):
    max_x, max_y, offset_x, offset_y = get_complex_frame(coord_dictionary)

    background = 0
    red = (255, 0, 0, 0)
    white = (255, 255, 255, 0)
    green = (0, 255, 0, 0)
    blue = (0, 0, 255, 0)

    im = Image.new('RGB', (max_x + offset_x + 1, max_y + offset_y + 1), color=background)

    for k, v in coord_dictionary.items():
        k = (int(k.real) + offset_x, int(k.imag) + offset_y)
        if v == "#":
            im.putpixel(k, red)
        elif v == ".":
            im.putpixel(k, white)
        elif v == "X":
            im.putpixel(k, green)
        else:
            im.putpixel(k, blue)

    h, w = im.size

    upsize = 10
    im = im.resize((h * upsize, w * upsize))
    im = ImageOps.flip(im)
    im.show()


# room = {1j: '#', (1+0j): '.', -1j: '.', (-1+0j): '.', (-1-1j): '.', (-1-2j): '.', -2j: '.', 0j: '.', (1+1j): '.', (1+2j): '.', (1+3j): '.'}
# room = {1j: '#', (1+0j): '#', -1j: '#', (-1+0j): '#', (-2+0j): '.', (-2-1j): '#', (-3+0j): '#', (-2+1j): '.', 0j: '.', (-1+1j): '.', (-1+2j): '#', (-2-2j): '.', (-2-3j): '.', (-1-3j): '.', -3j: '#', (-1-4j): '#', (-1-2j): '#', (-3-2j): '.', (-3-3j): '.', (-3-4j): '.', (-2-4j): '.', (-4-3j): '#', (-4-2j): '.', (-5-2j): '#', (-4-1j): '#', (-3-1j): '.'}
#
# screen_complex(room)


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


def get_parameters(intcode_list, raw, relative_base, mode):
    if mode == 0:
        return intcode_list[raw]
    if mode == 1:
        return raw
    if mode == 2:
        return intcode_list[raw + relative_base]


def get_write_parameters(intcode_list, raw, relative_base, mode):
    if mode == 0:
        return raw
    if mode == 1:
        return None
    if mode == 2:
        return raw + relative_base


def full_intcode_computer(ram, pointer, rb, loc={}):
    relative_base = rb
    counter = pointer
    if len(ram) < 100000:
        pre_buffer = [0 for x in range(10000)]
        ram.extend(pre_buffer)

    while True:
        try:
            item = ram[counter]

            ones = int(str(item)[-1])
            tens = int(str(item // 10)[-1])
            hundreds = int(str(item // 100)[-1])
            thousands = int(str(item // 1000)[-1])
            ten_thousands = int(str(item // 10000)[-1])

            if ones == 1:
                raw1 = ram[counter + 1]
                raw2 = ram[counter + 2]
                raw3 = ram[counter + 3]
                param1 = get_parameters(ram, raw1, relative_base, hundreds)
                param2 = get_parameters(ram, raw2, relative_base, thousands)
                param3 = get_write_parameters(ram, raw3, relative_base, ten_thousands)

                position = param3
                ram[position] = param1 + param2
                counter += 4
                continue

            if ones == 2:
                raw1 = ram[counter + 1]
                raw2 = ram[counter + 2]
                raw3 = ram[counter + 3]
                param1 = get_parameters(ram, raw1, relative_base, hundreds)
                param2 = get_parameters(ram, raw2, relative_base, thousands)
                param3 = get_write_parameters(ram, raw3, relative_base, ten_thousands)

                position = param3
                ram[position] = param1 * param2
                counter += 4
                continue

            if ones == 3:
                raw1 = ram[counter + 1]
                param1 = get_write_parameters(ram, raw1, relative_base, hundreds)
                ram[param1] = loc.get('my_input', 0)
                counter += 2
                continue

            if ones == 4:
                raw1 = ram[counter + 1]
                param1 = get_parameters(ram, raw1, relative_base, hundreds)

                # print(param1)
                counter += 2
                # input = loc.get('color', 0)

                yield param1

            if ones == 5:
                raw1 = ram[counter + 1]
                raw2 = ram[counter + 2]
                param1 = get_parameters(ram, raw1, relative_base, hundreds)
                param2 = get_parameters(ram, raw2, relative_base, thousands)

                if param1 == 0:
                    counter += 3
                else:
                    counter = param2
                    continue

            if ones == 6:
                raw1 = ram[counter + 1]
                raw2 = ram[counter + 2]
                param1 = get_parameters(ram, raw1, relative_base, hundreds)
                param2 = get_parameters(ram, raw2, relative_base, thousands)

                if param1 != 0:
                    counter += 3
                else:
                    counter = param2
                    continue

            if ones == 7:
                raw1 = ram[counter + 1]
                raw2 = ram[counter + 2]
                raw3 = ram[counter + 3]
                param1 = get_parameters(ram, raw1, relative_base, hundreds)
                param2 = get_parameters(ram, raw2, relative_base, thousands)
                param3 = get_write_parameters(ram, raw3, relative_base, ten_thousands)

                position = param3

                if param1 < param2:
                    ram[position] = 1
                else:
                    ram[position] = 0

                counter += 4
                continue

            if ones == 8:
                raw1 = ram[counter + 1]
                raw2 = ram[counter + 2]
                raw3 = ram[counter + 3]
                param1 = get_parameters(ram, raw1, relative_base, hundreds)
                param2 = get_parameters(ram, raw2, relative_base, thousands)
                param3 = get_write_parameters(ram, raw3, relative_base, ten_thousands)

                position = param3

                if param1 == param2:
                    ram[position] = 1
                else:
                    ram[position] = 0

                counter += 4
                continue

            if ones == 9 and tens == 9:
                return "Complete"

            if ones == 9:
                raw1 = ram[counter + 1]
                param1 = get_parameters(ram, raw1, relative_base, hundreds)

                relative_base += param1
                counter += 2
        except:
            print(counter)


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


def robot_turner(coord, direction, color):
    turn_map = {
        "N": ["W", "E"],
        "S": ["E", "W"],
        "W": ["S", "N"],
        "E": ["N", "S"]
    }

    d = turn_map[direction][color]

    # Directional Dictionary for Grid Movements
    DX = dict(zip('WENS', [-1, 1, 0, 0]))
    DY = dict(zip('WENS', [0, 0, 1, -1]))

    return (coord[0] + DX[d], coord[1] + DY[d]), d