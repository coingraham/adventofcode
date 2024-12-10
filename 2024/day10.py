from aocd.models import Puzzle
from multiprocessing import Pool
from os import cpu_count
from collections import deque
puzzle = Puzzle(year=2024, day=10)

sample_data = '''89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732'''

sample_data = '''..90..9
..51598
...2..7
6543456
765.987
876....
987....'''


from aoc_common import build_2_d_ints, identify_locations
# q_i = build_2_d_ints(sample_data)
q_i = build_2_d_ints(puzzle.input_data)
trail_items = identify_locations(q_i)


def get_next_step(q_i, current):
    options = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    point, level = current
    next_steps = []
    for option in options:
        this_step = (point[0] + option[0], point[1] + option[1])
        # check if valid
        if any(item < 0 or item >= len(q_i) for item in this_step):
            continue

        this_level = q_i[this_step[0]][this_step[1]]

        if level - this_level == 1:
            next_steps.append((this_step, this_level))

    return next_steps


def walk_trail_queue(start):
    queue = deque()
    queue.append((start, 9))

    paths = set()
    while queue:
        new_options = get_next_step(q_i, queue.pop())
        for item in new_options:
            if item[1] == 0:
                paths.add(item[0])
            else:
                queue.append(item)

    return len(paths)


def walk_trail_queue_p2(start):
    queue = deque()
    queue.append((start, 9))

    paths = 0
    while queue:
        new_options = get_next_step(q_i, queue.pop())
        for item in new_options:
            if item[1] == 0:
                paths += 1
            else:
                queue.append(item)

    return paths


def part_one(q_i, trail_items):
    threads = max(cpu_count() - 1, 1)
    total_trails = 0

    with Pool(threads) as pool:
        for values in pool.imap_unordered(walk_trail_queue, trail_items[9]):
                total_trails += values

    return total_trails


def part_two(q_i, trail_items):
    threads = max(cpu_count() - 1, 1)
    total_trails = 0

    # print(walk_trail_queue_p2(trail_items[9][0]))
    # print(walk_trail_queue_p2(trail_items[9][4]))

    with Pool(threads) as pool:
        for values in pool.imap_unordered(walk_trail_queue_p2, trail_items[9]):
                total_trails += values

    return total_trails


if __name__ == '__main__':
    # print(part_one(q_i, trail_items))
    print(part_two(q_i, trail_items))
