from typing import Mapping
from aocd.models import Puzzle
puzzle = Puzzle(year=2021, day=1)

# print(puzzle.input_data)

question_input = puzzle.input_data

sample_data = '''
199
200
208
210
200
207
240
269
260
263'''

# question_input = [int(n) for n in sample_data.split()]
question_input = [int(n) for n in question_input.split()]


def part_one():
    increased = 0
    for index, item in enumerate(question_input):
        if index == 0:
            continue

        if item > question_input[index - 1]:
            increased += 1

    return increased


def part_two():
    increased = 0
    previous_sum = 0
    for index, item in enumerate(question_input):
        if index < 3:
            previous_sum += item
            continue

        new_sum = item + previous_sum - question_input[index - 3]

        if new_sum > previous_sum:
            increased += 1

    previous_sum = new_sum

    return increased


if __name__ == '__main__':
    print(part_one())
    print(part_two())
