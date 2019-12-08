
import itertools

# puzzle = Puzzle(year=2019, day=7)

# print(puzzle.input_data)

input_data = """3,8,1001,8,10,8,105,1,0,0,21,34,43,60,81,94,175,256,337,418,99999,3,9,101,2,9,9,102,4,9,9,4,9,99,3,9,102,2,9,9,4,9,99,3,9,102,4,9,9,1001,9,4,9,102,3,9,9,4,9,99,3,9,102,4,9,9,1001,9,2,9,1002,9,3,9,101,4,9,9,4,9,99,3,9,1001,9,4,9,102,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,99"""


def intcode_computer(state, first, phase=None):
    intcode_list = state[0]
    counter = state[1]
    if phase:
        input = phase
    else:
        input = first
    output = first
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
                if phase:
                    input = first
                continue

            if ones == 4:
                if hundreds == 1:
                    param1 = intcode_list[counter + 1]
                else:
                    param1 = intcode_list[intcode_list[counter + 1]]

                # print(param1)
                output = param1
                counter += 2
                return [intcode_list, counter, False], output

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
                return [intcode_list, counter, True], output
    except:
        print(counter)

# test_input = "3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10"

intcode_list = input_data.split(",")

# test_list = test_input.split(",")

original_intcode_list = [int(x) for x in intcode_list]


def run_options(list):
    # Machine state, instruction point, quit
    first_state = [original_intcode_list.copy(), 0, False]
    second_state = [original_intcode_list.copy(), 0, False]
    third_state = [original_intcode_list.copy(), 0, False]
    fourth_state = [original_intcode_list.copy(), 0, False]
    fifth_state = [original_intcode_list.copy(), 0, False]

    fifth_output = 0
    first_run = True

    while True:
        if first_run:
            first_state, first_output = (intcode_computer(first_state, fifth_output, list[0]))
            second_state, second_output = (intcode_computer(second_state, first_output, list[1]))
            third_state, third_output = (intcode_computer(third_state, second_output, list[2]))
            fourth_state, fourth_output = (intcode_computer(fourth_state, third_output, list[3]))
            fifth_state, fifth_output = (intcode_computer(fifth_state, fourth_output, list[4]))
        else:
            first_state, first_output = (intcode_computer(first_state, fifth_output))
            second_state, second_output = (intcode_computer(second_state, first_output))
            third_state, third_output = (intcode_computer(third_state, second_output))
            fourth_state, fourth_output = (intcode_computer(fourth_state, third_output))
            fifth_state, fifth_output = (intcode_computer(fifth_state, fourth_output))

        first_run = False

        if fifth_state[2]:
            return fifth_output


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
max = 0
for i in itertools.permutations([5, 6, 7, 8, 9, ], 5):
    current = run_options(i)
    if current > max:
        max = current

print(max)