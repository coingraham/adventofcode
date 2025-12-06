from aocd.models import Puzzle
from aoc_common import build_2_d, get_8_directions
puzzle = Puzzle(year=2025, day=4)

sample_data = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

# question input
# q_i = build_2_d(sample_data)
q_i = build_2_d(puzzle.input_data)

directions = get_8_directions()

def part_one():
    number_of_free_rolls = 0

    # go through each position and find
    for x, row in enumerate(q_i):
        for y, item in enumerate(row):
            # continue if not a roll of paper
            if item != "@":
                continue
            
            # check each direction for rolls of paper
            rolls_around = 0

            for direction in directions:
                # get the next position
                next_x = x + direction[0]
                next_y = y + direction[1]

                # check if the next position is out of bounds
                if next_x < 0 or next_x >= len(q_i) or next_y < 0 or next_y >= len(q_i[0]):
                    continue

                # check if the next position is a roll of paper
                if q_i[next_x][next_y] == "@":
                    # if so, add 1 to the current position
                    rolls_around += 1

            if rolls_around < 4:
                number_of_free_rolls += 1
            
    return number_of_free_rolls
                

def part_two():
    
    number_of_free_rolls = 0
    updated = True

    while updated:
        updated = False

        # go through each position and find
        for x, row in enumerate(q_i):
            for y, item in enumerate(row):
                # continue if not a roll of paper
                if item != "@":
                    continue
                
                # check each direction for rolls of paper
                rolls_around = 0

                for direction in directions:
                    # get the next position
                    next_x = x + direction[0]
                    next_y = y + direction[1]

                    # check if the next position is out of bounds
                    if next_x < 0 or next_x >= len(q_i) or next_y < 0 or next_y >= len(q_i[0]):
                        continue

                    # check if the next position is a roll of paper
                    if q_i[next_x][next_y] == "@":
                        # if so, add 1 to the current position
                        rolls_around += 1

                if rolls_around < 4:
                    number_of_free_rolls += 1
                    updated = True
                    q_i[x][y] = "."
            
    return number_of_free_rolls


if __name__ == '__main__':
    print(part_one())
    print(part_two())
