def get_parameters(intcode_list, raw, relative_base, mode):
    if mode == 0:
        return intcode_list[raw]
    if mode == 1:
        return raw
    if mode == 2:
        return intcode_list[raw + relative_base]


def get_write_parameters(intcode_list, raw, relative_base, mode):
    if mode == 0:
        return raw
    if mode == 1:
        return None
    if mode == 2:
        return raw + relative_base


def full_intcode_computer(ram, pointer, rb, loc={}):
    relative_base = rb
    counter = pointer
    if len(ram) < 100000:
        pre_buffer = [0 for x in range(10000)]
        ram.extend(pre_buffer)

    while True:
        try:
            item = ram[counter]

            ones = int(str(item)[-1])
            tens = int(str(item // 10)[-1])
            hundreds = int(str(item // 100)[-1])
            thousands = int(str(item // 1000)[-1])
            ten_thousands = int(str(item // 10000)[-1])

            if ones == 1:
                raw1 = ram[counter + 1]
                raw2 = ram[counter + 2]
                raw3 = ram[counter + 3]
                param1 = get_parameters(ram, raw1, relative_base, hundreds)
                param2 = get_parameters(ram, raw2, relative_base, thousands)
                param3 = get_write_parameters(ram, raw3, relative_base, ten_thousands)

                position = param3
                ram[position] = param1 + param2
                counter += 4
                continue

            if ones == 2:
                raw1 = ram[counter + 1]
                raw2 = ram[counter + 2]
                raw3 = ram[counter + 3]
                param1 = get_parameters(ram, raw1, relative_base, hundreds)
                param2 = get_parameters(ram, raw2, relative_base, thousands)
                param3 = get_write_parameters(ram, raw3, relative_base, ten_thousands)

                position = param3
                ram[position] = param1 * param2
                counter += 4
                continue

            if ones == 3:
                raw1 = ram[counter + 1]
                param1 = get_write_parameters(ram, raw1, relative_base, hundreds)
                if not loc.get('inputs', None):
                    yield "Waiting for Input"
                my_input = loc.get('inputs', None)
                if isinstance(my_input, list):
                    my_input = my_input.pop(0)
                ram[param1] = my_input
                counter += 2
                continue

            if ones == 4:
                raw1 = ram[counter + 1]
                param1 = get_parameters(ram, raw1, relative_base, hundreds)
                counter += 2

                yield param1

            if ones == 5:
                raw1 = ram[counter + 1]
                raw2 = ram[counter + 2]
                param1 = get_parameters(ram, raw1, relative_base, hundreds)
                param2 = get_parameters(ram, raw2, relative_base, thousands)

                if param1 == 0:
                    counter += 3
                else:
                    counter = param2
                    continue

            if ones == 6:
                raw1 = ram[counter + 1]
                raw2 = ram[counter + 2]
                param1 = get_parameters(ram, raw1, relative_base, hundreds)
                param2 = get_parameters(ram, raw2, relative_base, thousands)

                if param1 != 0:
                    counter += 3
                else:
                    counter = param2
                    continue

            if ones == 7:
                raw1 = ram[counter + 1]
                raw2 = ram[counter + 2]
                raw3 = ram[counter + 3]
                param1 = get_parameters(ram, raw1, relative_base, hundreds)
                param2 = get_parameters(ram, raw2, relative_base, thousands)
                param3 = get_write_parameters(ram, raw3, relative_base, ten_thousands)

                position = param3

                if param1 < param2:
                    ram[position] = 1
                else:
                    ram[position] = 0

                counter += 4
                continue

            if ones == 8:
                raw1 = ram[counter + 1]
                raw2 = ram[counter + 2]
                raw3 = ram[counter + 3]
                param1 = get_parameters(ram, raw1, relative_base, hundreds)
                param2 = get_parameters(ram, raw2, relative_base, thousands)
                param3 = get_write_parameters(ram, raw3, relative_base, ten_thousands)

                position = param3

                if param1 == param2:
                    ram[position] = 1
                else:
                    ram[position] = 0

                counter += 4
                continue

            if ones == 9 and tens == 9:
                return "Complete"

            if ones == 9:
                raw1 = ram[counter + 1]
                param1 = get_parameters(ram, raw1, relative_base, hundreds)

                relative_base += param1
                counter += 2
        except Exception as e:
            print(counter)




def get_intcode(test, i, j):
    test[1] = i
    test[2] = j
    for tranche in [(test[x:x + 4]) for x in range(0, len(test) - 3, 4)]:
        if tranche[0] == 1:
            test[tranche[3]] = test[tranche[1]] + test[tranche[2]]
        if tranche[0] == 2:
            test[tranche[3]] = test[tranche[1]] * test[tranche[2]]
        if tranche[0] == 99:
            return test[0]


def intcode_computer(intcode_list, input):
    counter = 0
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

            if ones == 3:
                # if hundreds == 1:
                #     param1 = intcode_list[counter + 1]
                # else:
                #     param1 = intcode_list[intcode_list[counter + 1]]
                param1 = intcode_list[counter + 1]
                intcode_list[param1] = input
                counter += 2

            if ones == 4:
                if hundreds == 1:
                    param1 = intcode_list[counter + 1]
                else:
                    param1 = intcode_list[intcode_list[counter + 1]]

                print(param1)
                counter += 2

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

            if ones == 9 and tens == 9:
                print("Complete")
                break
    except:
        print(counter)