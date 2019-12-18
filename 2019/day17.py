from collections import defaultdict
from itertools import product

from aocd.models import Puzzle
import aoc_intcode as ac

puzzle = Puzzle(year=2019, day=17)

ram = [int(x) for x in puzzle.input_data.split(",")]

computer = ac.full_intcode_computer(ram, 0, 0, locals())

image = {}
my_input = None
pos = -1 + 0j
duster = None
while True:
    try:
        output = next(computer)
        pos += 1

        if output == 35:
            image[pos] = "#"
        elif output == 46:
            image[pos] = "."
        elif output == 94:
            image[pos] = "^"
            print("Duster: {}".format(pos))
            duster = pos
        elif output == 10:
            pos += 1j
            pos -= pos.real + 1
        else:
            print("Houston we have a problem: {}".format(output))
    except Exception as e:
        # print(e)
        break

# ac.screen_complex(image)

intersections = []
for k, v in image.items():
    if v == "#":
        try:
            if image[k + 1j] == "#" and image[k - 1j] == "#" and image[k + 1] == "#" and image[k - 1] == "#":
                intersections.append(k)
        except Exception as e:
            # print(e)
            continue


# for update in intersections:
#     image[update] = "X"
#
# ac.screen_complex(image)

# Part One
# total = 0
# for co in intersections:
#     alignment = co.real * co.imag
#     total += alignment
#
# print(total)

# Part Two
turn_right = {
    "north": "east",
    "south": "west",
    "east": "south",
    "west": "north"
}

turn_left = {
    "north": "west",
    "south": "east",
    "east": "north",
    "west": "south"
}

movement = {
    "north": 0 - 1j,
    "south": 0 + 1j,
    "east": 1 + 0j,
    "west": -1 + 0j
}

direction = "east"
turns = ["L", "R", "R", "L", "L", "R", "R", "L", "R", "R", "L", "L", "R", "R", "L", "R", "R", "R", "L", "L", "R", "L", "R", "R", "R", "L", "L", "L", "L", "R", "R", "L", "L", "e"]
steps = 0
turned = "R"
pathing = []
pos = duster
while turns:
    steps += 1
    potential_pos = pos + movement[direction]
    if potential_pos not in image or image[potential_pos] != "#":
        turn = turns.pop(0)
        if turn == "L":
            # print("{}: {}".format(turned, steps - 1))
            pathing.append("{}{}".format(turned, steps - 1))
            turned = "L"
            direction = turn_left[direction]
            steps = 0
            image[pos] = "^"
            # ac.screen_complex(image)
            image[pos] = "#"
        elif turn == "R":
            # print("{}: {}".format(turned, steps - 1))
            pathing.append("{}{}".format(turned, steps - 1))
            turned = "R"
            direction = turn_right[direction]
            steps = 0
            image[pos] = "^"
            # ac.screen_complex(image)
            image[pos] = "#"
        else:
            # print("{}: {}".format(turned, steps - 1))
            pathing.append("{}{}".format(turned, steps - 1))
            image[pos] = "^"
            # ac.screen_complex(image)
            image[pos] = "#"

    else:
        pos = potential_pos

# Part Two work
ram[0] = 2
compression = {}
size = len(pathing)

for y in range(size, 0, -1):
    for tranche in [(pathing[x:x + y]) for x in range(0, len(pathing) - (y - 1), 1)]:
        sub = "".join(tranche)
        if sub in compression:
            compression[sub] += 1
        else:
            compression[sub] = 1

eliminate = compression.copy()
for k, v in eliminate.items():
    if v == 1:
        del compression[k]

path_string = "".join(pathing)
compress_map = []


def check_chunk(check_string, chunk):
        return list(filter(None, check_string.split(chunk))), "".join(check_string.split(chunk))


def generate_compression(compression_string, compression, depth):
    for item in product(compression, repeat=depth):
        remaining_string = compression_string
        for i in range(depth):
            remaining_string = "".join(remaining_string.split(item[i]))

        if not remaining_string:
            yield item


for winners in generate_compression(path_string, compression, 4):
    # Pick based on criteria
    pass



for chunk in compression:
    remaining, remaining_string = check_chunk(path_string, chunk=chunk)
    for remains in remaining:
        leftovers, leftovers_string = check_chunk(remaining_string, chunk=remains)
        for left in leftovers:
            lastly, last_string = check_chunk(leftovers_string, chunk=left)
            if not len(last_string):
                compress_map.append(((chunk, "A"), (remains, "B"), (left, "C")))

final = []
for item in compress_map:
    save = True
    for potential in item:
        if len(potential[0]) >= 20:
            save = False

    pieces = [x[0] for x in item]
    for stuff in final:
        inside = [x[0] for x in stuff]
        inside.extend(pieces)
        if len(set(inside)) == len(pieces):
            save = False

    if save:
        final.append(item)

print(final[0])

for item in final[0]:
    path_string = path_string.replace(item[0], item[1])


code = [
    "A,B,A,B,A,C,A,C,B,C\n",
    "R,6,L,10,R,10,R,10\n",
    "L,10,L,12,R,10\n",
    "R,6,L,12,L,10\n",
    "y\n"
]

# code_ascii = [ord(y) for x in code for y in list(x)]
code_ascii = []
for x in code:
    code_ascii.append([ord(y) for y in list(x)])

# for char in code[0]:
#     print(ord(char))

# inputs = code_ascii.pop(0)
# new_computer = ac.full_intcode_computer(ram, 0, 0, locals())
#
# screen = []
# while True:
#     try:
#         output = next(new_computer)
#         if output == "Waiting for Input":
#             # print("".join(screen))
#             inputs = code_ascii.pop(0)
#         elif output == 10:
#             print("".join(screen))
#             screen = []
#         else:
#             screen.append(chr(output))
#     except Exception as e:
#         break
#
#
# print(output)










