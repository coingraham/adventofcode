from collections import defaultdict
from itertools import product

from aocd.models import Puzzle
import aoc_common as ac_common
import aoc_intcode as ac
import aoc_screen as screen

puzzle = Puzzle(year=2019, day=19)

ram = [int(x) for x in puzzle.input_data.split(",")]

computer = ac.full_intcode_computer(ram, 0, 0, locals())

inputs = []
beam_size = 100
map_list = ac_common.get_complex_matrix(beam_size, beam_size)


def check_left(coordinate):
    count = 0
    while True:
        count += 1
        coordinate += (-1 + 0j)
        if get_beam_symbol(coordinate, ram) != 1:
            return count


def check_up(coordinate):
    count = 0
    while True:
        count += 1
        coordinate += (0 - 1j)
        if get_beam_symbol(coordinate, ram) != 1:
            return count


def get_top_left(start, size):
    return start + (complex(-1, -1) * (size - 1))


def get_potential_ratio(beam_map):
    middle_coord = None
    beam_list = []
    for y in range(beam_size):
        location = complex(beam_size - 1, y)
        if beam_map[location] == 1:
            beam_list.append(location)

    half = len(beam_list)//2
    middle_coord = beam_list[half]
    return int(middle_coord.real), int(middle_coord.imag)


def get_beam_symbol(coord, ram):
    inputs = [int(coord.real), int(coord.imag)]
    new_ram = ram[:]
    computer = ac.full_intcode_computer(new_ram, 0, 0, locals())
    try:
        while True:
            output = next(computer)
    except Exception as e:
        return output


# beam_map = {}
# total = 0
# while map_list:
#     if len(inputs) == 0:
#         coords = map_list.pop(0)
#         inputs = [int(coords.real), int(coords.imag)]
#
#     new_ram = ram[:]
#     computer = ac.full_intcode_computer(new_ram, 0, 0, locals())
#
#     try:
#         output = next(computer)
#         computer = ""
#         if output == "Waiting for Input":
#             continue
#
#         else:
#             total += output
#             beam_map[coords] = output
#     except Exception as e:
#             continue
#
# # Part One
# print(total)
# screen.screen_complex(beam_map)

# Part Two
# x, y = get_potential_ratio(beam_map)
x, y = 99, 73
ratio = 2
try_me = complex(ratio * x, ratio * y)
new_ram = ram[:]
final = None

while True:
    try:
        if get_beam_symbol(try_me, new_ram):
            ups = check_up(try_me)
            lefts = check_left(try_me)

            if ups > 100:
                ups_offset = -int((ups / 2))
            elif ups < 100:
                ups_offset = 100 - ups
            else:
                ups_offset = 0

            if lefts > 100:
                lefts_offset = -int((lefts / 2))
            elif lefts < 100:
                lefts_offset = 100 - lefts
            else:
                lefts_offset = 0

            if ups == 100 and lefts == 100:
                final = try_me
                print("Final: {}".format(final))
                break

            try_me += complex(lefts_offset, ups_offset)

        else:
            print("Failed, try again: {}".format(try_me))
            try_me += complex(2, 1)
            new_ram = ram[:]
            continue
    except Exception as e:
        continue



# final = complex(1106+817j)
print(((int(final.real) - 99) * 10000) + ((int(final.imag)) - 99))

offset = {
    1: complex(0, -99),
    2: complex(-99, 0),
    3: complex(-99, -99)
}

for os in offset.values():
    print(get_beam_symbol(final + os, ram))
#
#
# for y in range(715, 817):
#     print([get_beam_symbol(complex(x, y), ram) for x in range(1000, 1106)])
