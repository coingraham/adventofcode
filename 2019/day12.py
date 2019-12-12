import aoc_common as ac
import numpy as np
from aocd.models import Puzzle

puzzle = Puzzle(year=2019, day=12)

test_input = """<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>"""

test2 = """<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>"""

ints = ac.ints(puzzle.input_data)


def get_gravity(set, old):
    vel = [get_offset(j, set[:,i]) for i in range(3) for j in set[:,i]]
    vel = np.array(vel).reshape(3, 4)
    return np.add(np.swapaxes(vel, 0, 1), old)


def get_offset(v, l):
    offset = 0
    for item in l:
        if v < item:
            offset += 1
        if v > item:
            offset -= 1
    return offset


def calc_pow(m, n):
    return sum([np.sum(m[i,:]) * np.sum(n[i,:]) for i in range(4)])


def get_repeater(m, n):
    s, p, v = 1, 0, 0
    orig_pos = m
    orig_vel = n
    while True:
        n = np.add([get_offset(i, m) for i in m], n)
        m = np.add(m, n)

        if np.array_equal(m, orig_pos) and np.array_equal(n, orig_vel):
            return s

        s += 1


pos = np.array(ints, int).reshape(4, 3)
vel = np.zeros((4, 3), int)

# Part One
step = 0
while True:

    vel = get_gravity(pos, vel)
    pos = np.add(pos, vel)
    step += 1
    if step == 1000:
        print(pos)
        print(vel)
        print("Power: {}".format(calc_pow(np.abs(pos), np.abs(vel))))
        break

# Part 2
print(np.lcm.reduce([get_repeater(pos[:,i], vel[:,i]) for i in range(3)]))
