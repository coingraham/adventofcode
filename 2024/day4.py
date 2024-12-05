from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=4)

# sample_data = '''M.S
# .A.
# M.S'''

# sample_data = '''.M.S......
# ..A..MSMS.
# .M.S.MAA..
# ..A.ASMSM.
# .M.S.M....
# ..........
# S.S.S.S.S.
# .A.A.A.A..
# M.M.M.M.M.
# ..........'''

sample_data = '''MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX'''

from aoc_common import build_2_d, get_8_directions
# word_puzzle = build_2_d(sample_data)
word_puzzle = build_2_d(puzzle.input_data)

eight_directions = get_8_directions()


def walk_8_directions(start, find):
    total = 0
    for direction in eight_directions:
        try:
            total += walk_this_direction(start, direction, find.copy())
        except IndexError:
            continue

    return total


def move_point(point, direction):
    return tuple(a + b for a, b in zip(point, direction))


def walk_this_direction(point, direction, find):

    try:
        this_letter = find.pop(0)

        if point[0] < 0 or point[1] < 0:
            return 0

        if word_puzzle[point[1]][point[0]] == this_letter:
            if not find:
                return 1
            else:
                return walk_this_direction(move_point(point, direction), direction, find)
        else:
            return 0

    except IndexError:
        raise IndexError


def part_one():
    find = ["X", "M", "A", "S"]

    xmas = 0

    # Double loop to walk through every step of the puzzle
    for y, row in enumerate(word_puzzle):
        for x, column in enumerate(row):
            # print(f"({x}, {y} is {column}")
            xmas += walk_8_directions((x, y), find)

    return xmas

def rotate(cross):
    return cross[1:] + cross[:1]


def chk_pt(point, letter):
    try:
        return word_puzzle[point[1]][point[0]] == letter
    except IndexError:
        return False


def check_xmas_cross(point):
    if not chk_pt(point, "A"):
        return 0

    cross = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
    total_crosses = 0

    for i in range(4):
        cross = rotate(cross)
        if (chk_pt(move_point(point, cross[0]), "M")
                and chk_pt(move_point(point, cross[1]), "M")
                and chk_pt(move_point(point, cross[2]), "S")
                and chk_pt(move_point(point, cross[3]), "S")):

            total_crosses += 1

    return total_crosses


def part_two():
    x_mas = 0

    # Double loop to walk through every step of the inner puzzle
    for y, row in enumerate(word_puzzle[1:-1]):
        for x, column in enumerate(row[1:-1]):
            x_mas += check_xmas_cross((x + 1, y + 1))

    return x_mas

if __name__ == '__main__':
    print(part_one())
    print(part_two())
