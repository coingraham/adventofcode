def process_groups_over_lines(input_list, row_split, line_split=None):

    local_collection = []
    temporary_grouping = []
    for line in input_list:

        if line == row_split:
            local_collection.append(temporary_grouping.copy())
            temporary_grouping.clear()

        else:
            if line_split:
                for split_line in line.split(line_split):
                    temporary_grouping.append(split_line)
            else:
                temporary_grouping.append(line)

    local_collection.append(temporary_grouping)

    return local_collection

# How to use
from aocd.models import Puzzle

puzzle4 = Puzzle(year=2020, day=4)
puzzle6 = Puzzle(year=2020, day=6)

print(process_groups_over_lines(puzzle4.input_data.split("\n"), '', " "))
print(process_groups_over_lines(puzzle6.input_data.split("\n"), ''))
