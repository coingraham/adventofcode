def process_groups_over_lines(input_list, chunk_split, row_split, line_split=None):

    input_chunks = input_list.split(chunk_split)

    local_collection = []
    temporary_grouping = []
    for chunk in input_chunks:

        for row in chunk.split(row_split):
            if line_split:
                for split_line in row.split(line_split):
                    temporary_grouping.append(split_line)
            else:
                temporary_grouping.append(row)

        local_collection.append(temporary_grouping.copy())
        temporary_grouping.clear()

    return local_collection


# How to use
from aocd.models import Puzzle

puzzle4 = Puzzle(year=2020, day=4)
puzzle6 = Puzzle(year=2020, day=6)

print(process_groups_over_lines(puzzle4.input_data, "\n\n", "\n", " "))
print(process_groups_over_lines(puzzle6.input_data, "\n\n", "\n"))


def get_complex_distance(complex1, complex2):
    return int(abs(complex1.real - complex2.real) + abs(complex1.imag - complex2.imag))
