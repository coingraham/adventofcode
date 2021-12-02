import math
from aocd.models import Puzzle
puzzle = Puzzle(year=2021, day=2)

# print(puzzle.input_data)

sample_data = '''forward 5
down 5
forward 8
up 3
down 8
forward 2'''

# question_input = [item for item in sample_data.splitlines()]
question_input = [item for item in puzzle.input_data.splitlines()]


def part_one():
    position = complex(0, 0)
    movement = {
        "forward": complex(1, 0),
        "backward": complex(-1, 0),
        "down": complex(0, 1),
        "up": complex(0, -1)
    }

    for line in question_input:
        command, amount = line.split(" ")
        position += (movement[command] * int(amount))
    
    return int(abs(position.real * position.imag))


def part_two():
    position = complex(0, 0)
    aim = 0
    movement = {
        "forward": complex(1, 0),
        "backward": complex(-1, 0),
        "down": complex(0, 1),
        "up": complex(0, -1)
    }

    for line in question_input:
        command, amount_text = line.split(" ")
        amount = int(amount_text)
        if command == "down":
            aim += amount
        if command == "up":
            aim -= amount
        if command == "forward":
            position += complex(amount, 0)
            position += complex(0, amount * aim)
        
    print(position)
    return int(abs(position.real * position.imag))


if __name__ == '__main__':
    print(part_one())
    print(part_two())
