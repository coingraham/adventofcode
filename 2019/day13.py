import aoc_common as ac
from aocd.models import Puzzle

puzzle = Puzzle(year=2019, day=13)

ram = [int(x) for x in puzzle.input_data.split(",")]
# pointer = 0
# relative_base = 0
# my_input = 0
#
# arcade = {}
# our_computer = ac.full_intcode_computer(ram, pointer, relative_base, locals())
#
# while True:
#     try:
#         x = next(our_computer)
#         y = next(our_computer)
#         z = next(our_computer)
#
#         arcade[(x, y)] = z
#     except:
#         break
#
# # Part One
# blocks = sum([ 1 for k, v in arcade.items() if v == 2])
# print(blocks)

pointer = 0
relative_base = 0
my_input = 0

paddle = None
ball = None
score = 0
ram = [int(x) for x in puzzle.input_data.split(",")]
ram[0] = 2
our_computer = ac.full_intcode_computer(ram, pointer, relative_base, locals())

try:
    while True:
        x = next(our_computer)
        y = next(our_computer)
        z = next(our_computer)

        if x == -1 and y == 0:
            score = z

        if z == 3:
            paddle = x

        if z == 4:
            ball = x

        if paddle and ball:
            if paddle > ball:
                my_input = -1
            elif ball > paddle:
                my_input = 1
            else:
                my_input = 0

except Exception as e:
    # print(e)
    pass

# Part Two - play the game and win
print(score)