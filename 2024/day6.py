from aocd.models import Puzzle
puzzle = Puzzle(year=2024, day=6)

sample_data = '''....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...'''

from aoc_common import build_2_d as b2d
# q_i = b2d(sample_data)
q_i = b2d(puzzle.input_data)

direction = {
    "^": ((-1, 0), "up"),
    ">": ((0, 1), "right"),
    "v": ((1, 0), "down"),
    "<": ((0, -1), "left"),
}

facing = {
    (-1, 0): "up",
    (0, 1): "right",
    (1, 0): "down",
    (0, -1): "left",
}

path = set()


def find_start_and_direction(a_map):
    for i, row in enumerate(a_map):
        for j, column in enumerate(row):
            if column in direction:
                return (i, j), direction[column][0]


def find_obstacles(a_map):
    obstacles = []

    for i, row in enumerate(a_map):
        for j, column in enumerate(row):
            if column == "#":
                obstacles.append((i, j))

    return obstacles


def turn_right(offset):
    turns = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    return turns[turns.index(offset) - 1]


def part_one(patrol):
    point, offset = find_start_and_direction(patrol)
    obstacles = find_obstacles(patrol)

    # walk as the security guard
    while True:
        next_point = (point[0] + offset[0], point[1] + offset[1])

        # check if obstacle
        if next_point in obstacles:
            offset = turn_right(offset)
            continue

        # try the next step, record if possible, return if not
        try:
            this = patrol[next_point[0]][next_point[1]]
            path.add(point)
            point = next_point

        except IndexError:
            path.add(point)
            break

    return len(path)


def turn_right_with_facing(offset):
    turns = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    new_offset = turns[turns.index(offset) - 1]
    return new_offset, facing[new_offset]


def check_patrol(patrol, point, offset, obstacles):
    facing = "up"
    path_facing = set()
    # walk as the security guard with new obstacles
    while True:
        next_point = (point[0] + offset[0], point[1] + offset[1])

        # check if looped
        if (point, facing) in path_facing:
            return 1

        # check if obstacle
        if next_point in obstacles:
            offset, facing = turn_right_with_facing(offset)
            continue

        # try the next step, record if possible, return if not
        try:
            this = patrol[next_point[0]][next_point[1]]
            path_facing.add((point, facing))
            point = next_point

        except IndexError:
            return 0


def part_two(patrol):
    point, offset = find_start_and_direction(patrol)
    obstacles = find_obstacles(patrol)
    loops = 0

    for i, step in enumerate(path):
        these_obstacles = obstacles.copy()
        these_obstacles.append(step)
        loops += check_patrol(patrol, point, offset, these_obstacles)

    return loops


if __name__ == '__main__':
    print(part_one(q_i.copy()))
    print(part_two(q_i.copy()))
