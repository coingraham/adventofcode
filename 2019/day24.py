from collections import deque

import aoc_common as ac

test = """....#
#..#.
#..##
..#..
#...."""

real = """..#.#
#.##.
.#..#
#....
....#"""

lines = real.splitlines()


def bugs(lines):
    grid = {}
    for y, line in enumerate(lines):
        for x, it in enumerate(line):
            location = complex(x+1, y+1)
            it = 1 if it == "#" else 0
            grid[location] = it
    return grid


def create_blank():
    grid = {}
    blanks = [[0 for x in range(5)] for y in range(5)]
    for y, blank in enumerate(blanks):
        for x, it in enumerate(blank):
            location = complex(x + 1, y + 1)
            grid[location] = it
    return grid


def process_grid(mg):
    new_mg = {}
    original = {}
    for k, v in mg.items():
        grid = v
        original[complex(3, 2)] = grid[complex(3, 2)]
        original[complex(2, 3)] = grid[complex(2, 3)]
        original[complex(3, 4)] = grid[complex(3, 4)]
        original[complex(4, 3)] = grid[complex(4, 3)]
        if k - 1 in mg.keys():
            # fill outers from upstream
            for i in range(1, 6):
                grid[complex(i, 0)] = mg[k - 1][complex(3, 2)]
                grid[complex(0, i)] = mg[k - 1][complex(2, 3)]
                grid[complex(i, 6)] = mg[k - 1][complex(3, 4)]
                grid[complex(6, i)] = mg[k - 1][complex(4, 3)]

        if k + 1 not in mg.keys():
            grid = check_bugs(grid)

        else:
            noc = sum(mg[k + 1][x] for x in [(1 + 1j), (2 + 1j), (3 + 1j), (4 + 1j), (5 + 1j)])
            noc += mg[k][complex(2, 2)] + mg[k][complex(3, 1)] + mg[k][complex(4, 2)]
            eoc = sum(mg[k + 1][x] for x in [(1 + 1j), (1 + 2j), (1 + 3j), (1 + 4j), (1 + 5j)])
            eoc += mg[k][complex(2, 2)] + mg[k][complex(1, 3)] + mg[k][complex(2, 4)]
            soc = sum(mg[k + 1][x] for x in [(1 + 5j), (2 + 5j), (3 + 5j), (4 + 5j), (5 + 5j)])
            soc += mg[k][complex(4, 4)] + mg[k][complex(3, 5)] + mg[k][complex(2, 4)]
            woc = sum(mg[k + 1][x] for x in [(5 + 1j), (5 + 2j), (5 + 3j), (5 + 4j), (5 + 5j)])
            woc += mg[k][complex(4, 4)] + mg[k][complex(5, 3)] + mg[k][complex(4, 2)]
            grid = check_bugs_rec(grid, noc, eoc, soc, woc)

            # for x, y, ds in [(3, 2, noc), (4, 3, woc), (3, 4, soc), (2, 3, eoc)]:
            #     if original[complex(x, y)] and ds == 1:
            #         grid[complex(x, y)] = 1
            #     elif not original[complex(x, y)] and 2 >= ds >= 1:
            #         grid[complex(x, y)] = 1
            #     else:
            #         grid[complex(x, y)] = 0

        grid[complex(3, 3)] = 0
        new_mg[k] = grid

    return new_mg


def check_bugs(grid):
    new_grid = {}
    check_list = [1, -1, 1j, -1j]
    for spot, bug in grid.items():
        sum = 0
        for check in check_list:
            this_spot = spot + check
            if this_spot in grid:
                sum += grid[this_spot]

        if bug and sum == 1:
            new_grid[spot] = 1
        elif not bug and 2 >= sum >= 1:
            new_grid[spot] = 1
        else:
            new_grid[spot] = 0
    return new_grid


def check_bugs_rec(grid, n, e, s, w):
    new_grid = {}
    check_list = [1, -1, 1j, -1j]
    for spot, bug in grid.items():
        total = 0

        if spot in [(3 + 2j), (4 + 3j), (3 + 4j), (2 + 3j)]:
            if spot == (3 + 2j):
                total = n
            if spot == (4 + 3j):
                total = w
            if spot == (3 + 4j):
                total = s
            if spot == (2 + 3j):
                total = e
        else:
            for check in check_list:
                this_spot = spot + check
                if this_spot in grid:
                    total += grid[this_spot]

        if bug and total == 1:
            new_grid[spot] = 1
        elif not bug and 2 >= total >= 1:
            new_grid[spot] = 1
        else:
            new_grid[spot] = 0
    new_grid[complex(3, 3)] = 0
    return new_grid


grid = bugs(lines)

# Part One
bug_list = []
while True:
    grid = check_bugs(grid)
    grid_string = "".join([str(x) for x in grid.values()])[::-1]
    b = (int(grid_string, 2))
    if b in bug_list:
        print(b)
        break
    else:
        bug_list.append(b)


# Part Two
grid = bugs(lines)
master_grid = {0: grid}
total = 0
counter = 1
while True:
    if counter % 2 == 1:
        mgk = list(master_grid.keys())
        master_grid[mgk[0] - 1] = create_blank()
        master_grid[mgk[-1] + 1] = create_blank()
        master_grid = {i: master_grid[i] for i in sorted(master_grid)}

    master_grid = process_grid(master_grid)
    master_grid = {i: master_grid[i] for i in sorted(master_grid)}
    if counter == 201:
        break
    counter += 1

    total = 0
    for k, v in master_grid.items():
        print("Depth: {}".format(k))
        for y in range(1, 6):
            # print(list(v[complex(x, y)] for x in range(1, 6)))
            total += sum(list(v[complex(x, y)] for x in range(1, 6)))

print(total)
