import aoc_common as ac
import numpy as np
from aocd.models import Puzzle

puzzle = Puzzle(year=2019, day=11)
ram = [int(x) for x in puzzle.input_data.split(",")]
pointer = 0
relative_base = 0


painting = {(0, 0): 0}
coord = (0, 0)
color = 0 # Part One
color = 1 # Part Two
direction = "N"

our_computer = ac.full_intcode_computer(ram, pointer, relative_base, locals())
while True:
    try:
        new_color = next(our_computer)
        d_color = next(our_computer)
        painting[coord] = new_color
        coord, direction = ac.robot_turner(coord, direction, d_color)
        if coord in painting:
            color = painting[coord]
        else:
            color = 0
    except:
        break

# print(len(painting.keys()))
x = []
y = []
z = []

for k, v in painting.items():
    x.append(int(k[0]))
    y.append(int(k[1]))
    z.append(int(v))

min_x = abs(min(x))
min_y = abs(min(y))
x = [i + min_x for i in x]
y = [j + min_y for j in y]

message = np.zeros([6, 43])
message[y, x] = z

message = np.where(message == 0, " ","■")

print(np.array2string(np.flipud(message), max_line_width=np.inf))






