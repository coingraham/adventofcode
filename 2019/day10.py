import aoc_common as ac
from collections import defaultdict
import math
from aocd.models import Puzzle

puzzle = Puzzle(year=2019, day=10)

# print(puzzle.input_data)

test_data = """.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##"""


def check_all(original_asteroid, asteroids):
    sd = {}
    altered_asteroids = [(x[0] - original_asteroid[0], x[1] - original_asteroid[1]) for x in asteroids]
    for alt_ast in altered_asteroids:
        if alt_ast == (0, 0):
            continue
        sd[math.atan2(alt_ast[1], alt_ast[0])] = alt_ast

    return(len(sd.keys()))


def laser(asteroids):
    lazered = []
    keep_all = defaultdict(dict)
    for asteroid in asteroids:
        if asteroid == (0, 0):
            continue
        rad = math.atan2(asteroid[0], asteroid[1])
        dist = math.hypot(asteroid[0], asteroid[1])
        keep_all[rad].update({dist: asteroid})

    keep_all = sorted(keep_all.items(), key=lambda tup: (tup[0], tup[1]))

    keep_all.reverse()

    while len(lazered) < 298:
        for radian in keep_all:
            dists = radian[1]
            if len(dists):
                k = list(dists.keys())[-1]
                v = dists[k]
                lazered.append(v)
                del radian[1][k]

    return lazered


# space = [list(i) for i in test_data.splitlines()]
space = [list(i) for i in puzzle.input_data.splitlines()]
asteroids = []

for coord in [(x, y) for y in range(len(space)) for x in range(len(space))]:
    if space[coord[1]][coord[0]] == "#":
        asteroids.append(coord)

total_seen = 0
top_asteroid = None
for asteroid in asteroids:
    seen = check_all(asteroid, asteroids)
    if seen > total_seen:
        total_seen = seen
        top_asteroid = asteroid

print(total_seen)
print(top_asteroid)

offset_asteroids = [(x[0] - top_asteroid[0], x[1] - top_asteroid[1]) for x in asteroids]

destroyed = laser(offset_asteroids)

un_offset = [(x[0] + top_asteroid[0], x[1] + top_asteroid[1]) for x in destroyed]

print(un_offset[199])





