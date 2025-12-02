from aocd.models import Puzzle
from collections import Counter
puzzle = Puzzle(year=2025, day=1)

sample_data = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""

# sample_data = """L150"""

# question input
# q_i = [n for n in sample_data.splitlines()]
q_i = [n for n in puzzle.input_data.splitlines()]

safe_options = [n for n in range(100)]

def part_one():
    position = 50

    for item in q_i:
        move = int(item[1:])
        if item.startswith('L'):
            position = safe_options[(position - move) % 100]
        else:
            position = safe_options[(position + move) % 100]

        if position == 0:
            yield 1

def part_two():
    position = 50

    for item in q_i:
        move = int(item[1:])
        if item.startswith('L'):
            for click in range(move):
                left = position - 1
                position = safe_options[left % 100]
                
                if position == 0:
                    yield 1
        else:
            for click in range(move):
                right = position + 1
                position = safe_options[right % 100]

                if position == 0:
                    yield 1


if __name__ == '__main__':
    # print(sum(part_one()))
    print(sum(part_two()))

