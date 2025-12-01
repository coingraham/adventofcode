from aocd.models import Puzzle
puzzle = Puzzle(year=2024, day=12)

sample_data = '''AAAA
BBCD
BBCC
EEEC'''

sample_data = '''OOOOO
OXOXO
OOOOO
OXOXO
OOOOO'''

sample_data = '''RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE'''

from aoc_common import build_2_d, identify_locations, get_point_offset
# q_i = build_2_d(sample_data)
q_i = build_2_d(puzzle.input_data)

letter_map = identify_locations(q_i)


def get_groupings(points):
    import copy
    groupings = {}
    full_points = copy.deepcopy(points)

    while points:
        p1 = points.pop(0)
        fences = 4
        neighbors = []
        for p2 in full_points:
            if p1 == p2:
                continue

            offset = get_point_offset(p2, p1)

            if offset == (0, 1) or offset == (1, 0):
                fences -= 1
                neighbors.append(p2)

        related = False
        for k, v in groupings.items():
            if any([x == y for x in neighbors for y in v["points"]]):
                related = True
                groupings[k]["points"].append(p1)
                groupings[k]["fences"] += fences
                break

        if not related:
            if lg_keys := list(groupings.keys()):
                last_key = lg_keys[-1] + 1
            else:
                last_key = 1

            groupings.update({
                last_key: {
                    "points": [p1],
                    "fences": fences
                }
            })

        for neighbor in neighbors:
            if neighbor in points and points.index(neighbor) != 0:
                n_index = points.index(neighbor)
                points.insert(0, points.pop(n_index))

    return groupings


def part_one(letter_map):
    total_price = 0

    # Iterate over the letters and group
    for letter, points in letter_map.items():
        group = get_groupings(points)

        letter_price = 0
        for k, v in group.items():
            letter_price += (v["fences"] * len(v["points"]))
            total_price += (v["fences"] * len(v["points"]))

        print(f"{letter} is {letter_price}")

    return total_price


def part_two():
    pass


if __name__ == '__main__':
    print(part_one(letter_map))
    # print(part_two())
