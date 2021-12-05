from aoc_common import create_matrix_from_dict
from aoc_common import print_matrix
from aocd.models import Puzzle
puzzle = Puzzle(year=2021, day=5)

sample_data = '''0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2'''

question_input = [n.split(" -> ") for n in sample_data.splitlines()]
# question_input = [n.split(" -> ") for n in puzzle.input_data.splitlines()]

number_list = ",".join([item for pair in question_input for item in pair])
max_size = max([int(n) for n in number_list.split(",")])


def add_to_map(my_map, coord):
    if coord in my_map:
        my_map[coord] += 1
    else:
        my_map[coord] = 1

    return my_map


def part_one():
    sea_map = {}
    for coordinates in question_input:
        x_coord = coordinates[0]
        y_coord = coordinates[1]
        x1, y1 = [int(n) for n in x_coord.split(",")]
        x2, y2 = [int(n) for n in y_coord.split(",")]

        if x1 == x2 or y1 == y2:
            sea_map = add_to_map(sea_map, x_coord)
            sea_map = add_to_map(sea_map, y_coord)

            if y1 < y2:
                for step in range(y1 + 1, y2):
                    sea_map = add_to_map(sea_map, "{},{}".format(x1, step))
            if y2 < y1:
                for step in range(y2 + 1, y1):
                    sea_map = add_to_map(sea_map, "{},{}".format(x1, step))
            if x1 < x2:
                for step in range(x1 + 1, x2):
                    sea_map = add_to_map(sea_map, "{},{}".format(step, y1))
            if x2 < x1:
                for step in range(x2 + 1, x1):
                    sea_map = add_to_map(sea_map, "{},{}".format(step, y1))

    return len([n for n in sea_map.values() if n > 1])


def part_two():
    sea_map_part_two = {}
    for coordinates in question_input:
        x_coord = coordinates[0]
        y_coord = coordinates[1]
        x1, y1 = [int(n) for n in x_coord.split(",")]
        x2, y2 = [int(n) for n in y_coord.split(",")]

        sea_map_part_two = add_to_map(sea_map_part_two, x_coord)
        sea_map_part_two = add_to_map(sea_map_part_two, y_coord)

        if x1 == x2 or y1 == y2:
            if y1 < y2:
                for step in range(y1 + 1, y2):
                    sea_map_part_two = add_to_map(sea_map_part_two, "{},{}".format(x1, step))
            if y2 < y1:
                for step in range(y2 + 1, y1):
                    sea_map_part_two = add_to_map(sea_map_part_two, "{},{}".format(x1, step))
            if x1 < x2:
                for step in range(x1 + 1, x2):
                    sea_map_part_two = add_to_map(sea_map_part_two, "{},{}".format(step, y1))
            if x2 < x1:
                for step in range(x2 + 1, x1):
                    sea_map_part_two = add_to_map(sea_map_part_two, "{},{}".format(step, y1))
        else:
            min_x = min([x1, x2])
            max_x = max([x1, x2])

            if (x1 > x2 and y1 > y2) or (x1 < x2 and y1 < y2):
                min_y = min([y1, y2])
                for i, step in enumerate(range(min_x + 1, max_x)):
                    sea_map_part_two = add_to_map(sea_map_part_two, "{},{}".format(step, min_y + i + 1))
            else:
                max_y = max([y1, y2])
                for i, step in enumerate(range(min_x + 1, max_x)):
                    sea_map_part_two = add_to_map(sea_map_part_two, "{},{}".format(step, max_y - i - 1))

    matrix = create_matrix_from_dict(sea_map_part_two, max_size)
    print("\n{}\n".format(print_matrix(matrix)))
    return len([n for n in sea_map_part_two.values() if n > 1])


if __name__ == '__main__':
    print(part_one())
    print(part_two())
