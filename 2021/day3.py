from aocd.models import Puzzle
puzzle = Puzzle(year=2021, day=3)

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
question_input = [list(n) for n in puzzle.input_data.split()]


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

        max_alpha = max(set(temp), key=temp.count)
        gamma.append(actual[max_alpha])
        epsilon.append(opposite[max_alpha])
        temp = []
    
    gamma_num = int("".join(gamma), 2)
    epsilon_num = int("".join(epsilon), 2)
    return gamma_num * epsilon_num


def part_two(question_input):
    cycles = len(question_input[0])
    oxygen = question_input.copy()
    co = question_input.copy()
    zero_list = []
    one_list = []
    temp = []
    oxy_result = 0
    co_result = 0

    for i in range(cycles):
        for numbers in oxygen:
            temp.append(numbers[i])
            if numbers[i] == "0":
                zero_list.append(numbers)
            else:
                one_list.append(numbers)

        if temp.count("0") > temp.count("1"):
            if len(zero_list) == 1:
                oxy_result = int("".join(zero_list[0]), 2)
                break
            oxygen = zero_list
            zero_list = []
            one_list = []
            temp = []
        else:
            if len(one_list) == 1:
                oxy_result = int("".join(one_list[0]), 2)
                break
            oxygen = one_list
            zero_list = []
            one_list = []
            temp = []

    for i in range(cycles):
        for numbers in co:
            temp.append(numbers[i])
            if numbers[i] == "0":
                zero_list.append(numbers)
            else:
                one_list.append(numbers)

        if temp.count("0") <= temp.count("1"):
            if len(zero_list) == 1:
                co_result = int("".join(zero_list[0]), 2)
                break
            co = zero_list
            zero_list = []
            one_list = []
            temp = []
        else:
            if len(one_list) == 1:
                co_result = int("".join(one_list[0]), 2)
                break
            co = one_list
            zero_list = []
            one_list = []
            temp = []

    return oxy_result * co_result


if __name__ == '__main__':
    print(part_one())
    print(part_two(question_input))
