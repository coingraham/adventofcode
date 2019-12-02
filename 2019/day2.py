import aoc_common as ac
from aocd.models import Puzzle

puzzle = Puzzle(year=2019, day=2)

puzzle_input = [int(x) for x in puzzle.input_data.split(",")]

# Part One
testing = puzzle_input.copy()
print(ac.get_intcode(testing, 12, 2))
# puzzle.answer_a = 7594646

# Part Two
for x in range(100):
    for y in range(100):
        testing = puzzle_input.copy()
        if ac.get_intcode(testing, x, y) == 19690720:
            print(100 * x + y)
            # puzzle.answer_b = 3376
