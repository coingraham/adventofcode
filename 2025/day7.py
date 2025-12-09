from aocd.models import Puzzle
from aoc_common import build_2_d, print_matrix
from collections import defaultdict

puzzle = Puzzle(year=2025, day=7)

sample_data = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""

# question input
# q_i = build_2_d(sample_data)
q_i = build_2_d(puzzle.input_data)

def part_one():
    # walk the grid from top to bottom and react to items you find
    total_splits = 0
    for y, row in enumerate(q_i):
        for x, item in enumerate(row):
            if item == 'S':
                q_i[y + 1][x] = "|"

            if y > 0 and q_i[y - 1][x] == "|" and item != '^':
                q_i[y][x] = "|"

            if item == '^' and q_i[y - 1][x] == "|":
                q_i[y][x - 1] = "|"
                q_i[y][x + 1] = "|"
                total_splits += 1
                
        print_matrix(q_i)

    return total_splits
                

def part_two():
    # walk the grid from top to bottom and react to items you find
    paths = {}

    for y, row in enumerate(q_i):
        print_matrix(q_i)
        print(paths)
        print(sum(paths.values()))
        print("")
        for x, item in enumerate(row):
            if item == 'S':
                q_i[y + 1][x] = "|"
                paths[(y + 1, x)] = 1

            if y > 0 and q_i[y - 1][x] == "|" and item != '^':
                q_i[y][x] = "|"
                if (y, x) not in paths:
                    paths[(y, x)] = paths[(y - 1, x)]
                else:
                    paths[(y, x)] += paths[(y - 1, x)]

                del paths[(y - 1, x)]

            if item == '^' and q_i[y - 1][x] == "|":
                q_i[y][x - 1] = "|"
                q_i[y][x + 1] = "|"
                paths = update_paths(paths, (y - 1, x), [(y, x - 1), (y, x + 1)])
                

    return sum(paths.values())


def update_paths(paths, search, updates):
    # Check for search in paths keys
    if search in paths:
        for update in updates:
            if update not in paths:
                paths[update] = paths[search]
            else:
                paths[update] += paths[search]

        del paths[search]

    return paths


def part_two_alternative():
    # walk the grid from top to bottom and react to items you find
    paths = [[]]

    for y, row in enumerate(q_i):
        print_matrix(q_i)
        print(", ".join([str(path) for path in paths]))
        print(len(paths))
        print("")
        for x, item in enumerate(row):
            if item == 'S':
                q_i[y + 1][x] = "|"
                paths = [[(y + 1, x)]]

            if y > 0 and q_i[y - 1][x] == "|" and item != '^':
                q_i[y][x] = "|"
                paths = search_paths_and_update(paths, (y - 1, x), [(y, x)])

            if item == '^' and q_i[y - 1][x] == "|":
                q_i[y][x - 1] = "|"
                q_i[y][x + 1] = "|"
                paths = search_paths_and_update(paths, (y - 1, x), [(y, x - 1), (y, x + 1)])

    return len(paths)


# This is way too slow... abandoning
def search_paths_and_update(paths, search, update):
    for path in paths:
        if path[-1] == search:
            if len(update) == 1:
                path.append(update[0])
            else:
                this = path.copy()
                path.append(update[0])
                this.append(update[1])
                paths.insert(0, this)

    return paths

if __name__ == '__main__':
    # print(part_one())
    print(part_two())
    # print(part_two_alternative())

