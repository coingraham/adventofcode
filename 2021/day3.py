from collections import Counter
from aocd.models import Puzzle
puzzle = Puzzle(year=2021, day=3) 

question_input = puzzle.input_data

sample_data = '''00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010'''

# question_input = [list(n) for n in sample_data.split()]
question_input = [list(n) for n in question_input.split()]


def part_one():
    gamma = []
    epsilon = []
    temp = []

    actual = {
        "0": "0",
        "1": "1"
    }

    opposite = {
        "0": "1",
        "1": "0"
    }

    for i in range(len(question_input[0])):
        for numbers in question_input:
            temp.append(numbers[i])

        max_alpha = max(set(temp), key = temp.count)
        gamma.append(actual[max_alpha])
        epsilon.append(opposite[max_alpha])
        temp = []
    
    gamma_num = int("".join(gamma), 2)
    epsilon_num = int("".join(epsilon), 2)
    return gamma_num * epsilon_num



def part_two():
    pass


if __name__ == '__main__':
    print(part_one())
    print(part_two())
