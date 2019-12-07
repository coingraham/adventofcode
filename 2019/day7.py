import aoc_common as ac
import itertools
from aocd.models import Puzzle

puzzle = Puzzle(year=2019, day=7)

# print(puzzle.input_data)



def intcode_computer(intcode_list, first, second=None):
    counter = 0
    input = first
    output = []
    try:
        while True:

            item = intcode_list[counter]

            ones = int(str(item)[-1])
            tens = int(str(item // 10)[-1])
            hundreds = int(str(item // 100)[-1])
            thousands = int(str(item // 1000)[-1])

            if ones == 1:
                if hundreds == 1:
                    param1 = intcode_list[counter + 1]
                else:
                    position = intcode_list[counter + 1]
                    param1 = intcode_list[position]

                if thousands == 1:
                    param2 = intcode_list[counter + 2]
                else:
                    param2 = intcode_list[intcode_list[counter + 2]]

                intcode_list[intcode_list[counter + 3]] = param1 + param2
                counter += 4
                continue

            if ones == 2:
                if hundreds == 1:
                    param1 = intcode_list[counter + 1]
                else:
                    param1 = intcode_list[intcode_list[counter + 1]]

                if thousands == 1:
                    param2 = intcode_list[counter + 2]
                else:
                    param2 = intcode_list[intcode_list[counter + 2]]

                intcode_list[intcode_list[counter + 3]] = param1 * param2
                counter += 4
                continue

            if ones == 3:
                # if hundreds == 1:
                #     param1 = intcode_list[counter + 1]
                # else:
                #     param1 = intcode_list[intcode_list[counter + 1]]
                param1 = intcode_list[counter + 1]
                intcode_list[param1] = input
                counter += 2
                if second:
                    input = second.pop(0)
                continue

            if ones == 4:
                if hundreds == 1:
                    param1 = intcode_list[counter + 1]
                else:
                    param1 = intcode_list[intcode_list[counter + 1]]

                # print(param1)
                output.append(param1)
                counter += 2
                continue

            if ones == 5:
                if hundreds == 1:
                    param1 = intcode_list[counter + 1]
                else:
                    param1 = intcode_list[intcode_list[counter + 1]]

                if thousands == 1:
                    param2 = intcode_list[counter + 2]
                else:
                    param2 = intcode_list[intcode_list[counter + 2]]

                if param1 == 0:
                    counter += 3
                else:
                    counter = param2
                    continue

            if ones == 6:
                if hundreds == 1:
                    param1 = intcode_list[counter + 1]
                else:
                    param1 = intcode_list[intcode_list[counter + 1]]

                if thousands == 1:
                    param2 = intcode_list[counter + 2]
                else:
                    param2 = intcode_list[intcode_list[counter + 2]]

                if param1 != 0:
                    counter += 3
                else:
                    counter = param2
                    continue

            if ones == 7:
                if hundreds == 1:
                    param1 = intcode_list[counter + 1]
                else:
                    param1 = intcode_list[intcode_list[counter + 1]]

                if thousands == 1:
                    param2 = intcode_list[counter + 2]
                else:
                    param2 = intcode_list[intcode_list[counter + 2]]

                if param1 < param2:
                    intcode_list[intcode_list[counter + 3]] = 1
                else:
                    intcode_list[intcode_list[counter + 3]] = 0

                counter += 4
                continue

            if ones == 8:
                if hundreds == 1:
                    param1 = intcode_list[counter + 1]
                else:
                    param1 = intcode_list[intcode_list[counter + 1]]

                if thousands == 1:
                    param2 = intcode_list[counter + 2]
                else:
                    param2 = intcode_list[intcode_list[counter + 2]]

                if param1 == param2:
                    intcode_list[intcode_list[counter + 3]] = 1
                else:
                    intcode_list[intcode_list[counter + 3]] = 0

                counter += 4
                continue

            if ones == 9 and tens == 9:
                # print("Complete")
                return output
    except:
        print(counter)

test_input = "3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10"

intcode_list = puzzle.input_data.split(",")

test_list = test_input.split(",")

original_intcode_list = [ int(x) for x in test_list]


def run_options(list, start, initial):
    if initial:
        first = (intcode_computer(original_intcode_list.copy(), start))
    else:
        first = (intcode_computer(original_intcode_list.copy(), list[0], start))
    # print(first)
    second = (intcode_computer(original_intcode_list.copy(), list[1], first))
    # print(second)
    third =(intcode_computer(original_intcode_list.copy(), list[2], second))
    # print(third)
    fourth = (intcode_computer(original_intcode_list.copy(), list[3], third))
    # print(fourth)
    fifth = (intcode_computer(original_intcode_list.copy(), list[4], fourth))

    return fifth


# Part One
# max = 0
# for i in itertools.permutations([0, 1, 2, 3, 4], 5):
#     current = run_options(i)
#     if current > max:
#         max = current
#
# print(max)
#
# puzzle.answer_a = max

# Part Two
# max = 0
# for i in itertools.permutations([5, 6, 7, 8, 9], 5):
#     start = 0
#     initial = True
#     while True:
#         current = run_options(i, start, initial)
#         start = current
#         initial = False
#         if current > max:
#             max = current


max = 0
start = 0
initial = True
while True:
    current = run_options([9,7,8,5,6], start, initial)
    start = current
    initial = False
    print(current)

# print(max)