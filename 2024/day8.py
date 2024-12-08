from aocd.models import Puzzle
puzzle = Puzzle(year=2024, day=8)

sample_data = '''............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............'''

# sample_data = '''.....
# .....
# ..A..
# .AAA.
# .....
# .....'''

sample_data = '''.........
A.A...A.A
.........'''

sample_data = '''...AA
...AA
.....'''

sample_data = '''........
..BABA..
........'''


from aoc_common import build_2_d, print_matrix, identify_locations
q_i = build_2_d(sample_data)
# q_i = build_2_d(puzzle.input_data)

print_matrix(q_i)

mapping = identify_locations(q_i)

def part_one(mapping):
    antinodes = set()

    for k, v in mapping.items():
        if k == '.':
            continue

        for antenna in v:
            for alternate in v:
                if antenna == alternate:
                    continue
                diff = tuple(a - b for a, b in zip(antenna, alternate))
                new = tuple(a + b for a, b in zip(antenna, diff))

                if any(new in sub for sub in mapping.values()):
                    antinodes.add(new)

    return len(antinodes)


def part_two(mapping):
    antinodes = set()

    for k, v in mapping.items():
        if k == '.':
            continue

        for antenna in v:
            for alternate in v:
                if antenna == alternate:
                    continue

                diff = tuple(a - b for a, b in zip(antenna, alternate))
                new = tuple(a + b for a, b in zip(antenna, diff))

                while any(new in sub for sub in mapping.values()):
                    antinodes.add(new)
                    antinodes.add(antenna)
                    antinodes.add(alternate)

                    new = tuple(a + b for a, b in zip(new, diff))

    return len(antinodes)


if __name__ == '__main__':
    print(part_one(mapping))
    print(part_two(mapping))
