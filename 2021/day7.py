from aocd.models import Puzzle
puzzle = Puzzle(year=2021, day=7)

sample_data = '''16,1,2,0,4,2,7,1,2,14'''

# question_input = [int(n) for n in sample_data.split(",")]
question_input = [int(n) for n in puzzle.input_data.split(",")]


def part_one(crabs_position_list):

    minimum = float("inf")
    for position in range(crabs_position_list[0], crabs_position_list[-1]):
        distance = 0
        for crab in crabs_position_list:
            if crab > position:
                distance += (crab - position)
            if position > crab:
                distance += (position - crab)
        
        if distance < minimum:
            minimum = distance

    return minimum


def fib_dict_builder(n):
    fib_dict = {0: 0}
    for step in range(1, n + 1):
        fib_dict[step] = fib_dict[step - 1] + step

    return fib_dict

def part_two(crabs_position_list):
    fib_cache = fib_dict_builder(crabs_position_list[-1])
    minimum = float("inf")
    for position in range(crabs_position_list[0], crabs_position_list[-1]):
        distance = 0
        for crab in crabs_position_list:
            if crab > position:
                diff = crab - position
                distance += fib_cache[diff]
            if position > crab:
                diff = position - crab
                distance += fib_cache[diff]
        
        if distance < minimum:
            minimum = distance

    return minimum


if __name__ == '__main__':
    question_input.sort()
    print(part_one(question_input))
    print(part_two(question_input))
