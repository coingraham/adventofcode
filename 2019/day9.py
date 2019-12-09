
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


def intcode_computer(intcode_list, input):
    relative_base = 0
    counter = 0
    pre_buffer = [0 for x in range(100000)]
    intcode_list.extend(pre_buffer)
    while True:
        try:

            item = intcode_list[counter]

            ones = int(str(item)[-1])
            tens = int(str(item // 10)[-1])
            hundreds = int(str(item // 100)[-1])
            thousands = int(str(item // 1000)[-1])
            ten_thousands = int(str(item // 10000)[-1])

            if ones == 1:
                raw1 = intcode_list[counter + 1]
                raw2 = intcode_list[counter + 2]
                raw3 = intcode_list[counter + 3]
                param1 = get_parameters(intcode_list, raw1, relative_base, hundreds)
                param2 = get_parameters(intcode_list, raw2, relative_base, thousands)
                param3 = get_write_parameters(intcode_list, raw3, relative_base, ten_thousands)

                position = param3
                intcode_list[position] = param1 + param2
                counter += 4
                continue

            if ones == 2:
                raw1 = intcode_list[counter + 1]
                raw2 = intcode_list[counter + 2]
                raw3 = intcode_list[counter + 3]
                param1 = get_parameters(intcode_list, raw1, relative_base, hundreds)
                param2 = get_parameters(intcode_list, raw2, relative_base, thousands)
                param3 = get_write_parameters(intcode_list, raw3, relative_base, ten_thousands)

                position = param3
                intcode_list[position] = param1 * param2
                counter += 4
                continue

            if ones == 3:
                raw1 = intcode_list[counter + 1]
                param1 = get_write_parameters(intcode_list, raw1, relative_base, hundreds)
                intcode_list[param1] = input
                counter += 2
                continue

            if ones == 4:
                raw1 = intcode_list[counter + 1]
                param1 = get_parameters(intcode_list, raw1, relative_base, hundreds)

                print(param1)
                counter += 2
                continue

            if ones == 5:
                raw1 = intcode_list[counter + 1]
                raw2 = intcode_list[counter + 2]
                param1 = get_parameters(intcode_list, raw1, relative_base, hundreds)
                param2 = get_parameters(intcode_list, raw2, relative_base, thousands)

                if param1 == 0:
                    counter += 3
                else:
                    counter = param2
                    continue

            if ones == 6:
                raw1 = intcode_list[counter + 1]
                raw2 = intcode_list[counter + 2]
                param1 = get_parameters(intcode_list, raw1, relative_base, hundreds)
                param2 = get_parameters(intcode_list, raw2, relative_base, thousands)

                if param1 != 0:
                    counter += 3
                else:
                    counter = param2
                    continue

            if ones == 7:
                raw1 = intcode_list[counter + 1]
                raw2 = intcode_list[counter + 2]
                raw3 = intcode_list[counter + 3]
                param1 = get_parameters(intcode_list, raw1, relative_base, hundreds)
                param2 = get_parameters(intcode_list, raw2, relative_base, thousands)
                param3 = get_write_parameters(intcode_list, raw3, relative_base, ten_thousands)

                position = param3

                if param1 < param2:
                    intcode_list[position] = 1
                else:
                    intcode_list[position] = 0

                counter += 4
                continue

            if ones == 8:
                raw1 = intcode_list[counter + 1]
                raw2 = intcode_list[counter + 2]
                raw3 = intcode_list[counter + 3]
                param1 = get_parameters(intcode_list, raw1, relative_base, hundreds)
                param2 = get_parameters(intcode_list, raw2, relative_base, thousands)
                param3 = get_write_parameters(intcode_list, raw3, relative_base, ten_thousands)

                position = param3

                if param1 == param2:
                    intcode_list[position] = 1
                else:
                    intcode_list[position] = 0

                counter += 4
                continue

            if ones == 9 and tens == 9:
                # print(output)
                return "Complete"

            if ones == 9:
                raw1 = intcode_list[counter + 1]
                param1 = get_parameters(intcode_list, raw1, relative_base, hundreds)

                relative_base += param1
                counter += 2
        except:
            print(counter)

input_data = """109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99"""
input_data2 = """1102,34915192,34915192,7,4,7,99,0"""
input_data3 = """104,1125899906842624,99"""
real_data = """1102,34463338,34463338,63,1007,63,34463338,63,1005,63,53,1102,3,1,1000,109,988,209,12,9,1000,209,6,209,3,203,0,1008,1000,1,63,1005,63,65,1008,1000,2,63,1005,63,904,1008,1000,0,63,1005,63,58,4,25,104,0,99,4,0,104,0,99,4,17,104,0,99,0,0,1102,521,1,1028,1101,0,36,1000,1102,30,1,1005,1101,21,0,1013,1101,26,0,1006,1102,31,1,1017,1101,24,0,1007,1101,0,1,1021,1102,27,1,1019,1101,23,0,1010,1101,0,38,1012,1102,35,1,1001,1101,25,0,1003,1102,20,1,1004,1101,0,37,1009,1101,424,0,1023,1102,39,1,1008,1102,406,1,1027,1102,1,413,1026,1101,0,29,1002,1102,1,0,1020,1102,34,1,1014,1102,1,28,1018,1102,1,33,1011,1102,300,1,1025,1102,1,22,1015,1102,305,1,1024,1101,32,0,1016,1102,427,1,1022,1101,512,0,1029,109,14,1205,6,197,1001,64,1,64,1106,0,199,4,187,1002,64,2,64,109,-18,1207,8,19,63,1005,63,215,1105,1,221,4,205,1001,64,1,64,1002,64,2,64,109,10,1208,-1,28,63,1005,63,237,1106,0,243,4,227,1001,64,1,64,1002,64,2,64,109,-2,2102,1,0,63,1008,63,22,63,1005,63,263,1105,1,269,4,249,1001,64,1,64,1002,64,2,64,109,11,21107,40,39,0,1005,1015,289,1001,64,1,64,1106,0,291,4,275,1002,64,2,64,109,9,2105,1,0,4,297,1105,1,309,1001,64,1,64,1002,64,2,64,109,-13,2101,0,-5,63,1008,63,25,63,1005,63,329,1105,1,335,4,315,1001,64,1,64,1002,64,2,64,109,1,1206,8,353,4,341,1001,64,1,64,1105,1,353,1002,64,2,64,109,3,2108,37,-6,63,1005,63,375,4,359,1001,64,1,64,1106,0,375,1002,64,2,64,109,-16,1207,2,36,63,1005,63,397,4,381,1001,64,1,64,1105,1,397,1002,64,2,64,109,28,2106,0,0,1001,64,1,64,1106,0,415,4,403,1002,64,2,64,109,-3,2105,1,-1,1106,0,433,4,421,1001,64,1,64,1002,64,2,64,109,-12,2108,25,-6,63,1005,63,449,1105,1,455,4,439,1001,64,1,64,1002,64,2,64,109,-19,1202,8,1,63,1008,63,38,63,1005,63,479,1001,64,1,64,1105,1,481,4,461,1002,64,2,64,109,14,2107,25,0,63,1005,63,497,1105,1,503,4,487,1001,64,1,64,1002,64,2,64,109,24,2106,0,-3,4,509,1001,64,1,64,1105,1,521,1002,64,2,64,109,-20,1208,-2,37,63,1005,63,543,4,527,1001,64,1,64,1106,0,543,1002,64,2,64,109,7,21102,41,1,0,1008,1018,43,63,1005,63,563,1105,1,569,4,549,1001,64,1,64,1002,64,2,64,109,-7,1205,10,587,4,575,1001,64,1,64,1106,0,587,1002,64,2,64,109,-11,1202,5,1,63,1008,63,30,63,1005,63,609,4,593,1106,0,613,1001,64,1,64,1002,64,2,64,109,4,1201,5,0,63,1008,63,34,63,1005,63,637,1001,64,1,64,1105,1,639,4,619,1002,64,2,64,109,12,1206,5,651,1105,1,657,4,645,1001,64,1,64,1002,64,2,64,109,9,21101,42,0,-7,1008,1018,39,63,1005,63,677,1105,1,683,4,663,1001,64,1,64,1002,64,2,64,109,-2,21101,43,0,-8,1008,1015,43,63,1005,63,705,4,689,1106,0,709,1001,64,1,64,1002,64,2,64,109,-25,2107,38,10,63,1005,63,727,4,715,1106,0,731,1001,64,1,64,1002,64,2,64,109,7,2102,1,2,63,1008,63,24,63,1005,63,757,4,737,1001,64,1,64,1105,1,757,1002,64,2,64,109,-13,1201,10,0,63,1008,63,29,63,1005,63,779,4,763,1105,1,783,1001,64,1,64,1002,64,2,64,109,30,21108,44,41,-3,1005,1019,803,1001,64,1,64,1106,0,805,4,789,1002,64,2,64,109,-2,21102,45,1,-7,1008,1013,45,63,1005,63,827,4,811,1105,1,831,1001,64,1,64,1002,64,2,64,109,-16,21107,46,47,7,1005,1011,849,4,837,1106,0,853,1001,64,1,64,1002,64,2,64,109,9,21108,47,47,0,1005,1013,875,4,859,1001,64,1,64,1106,0,875,1002,64,2,64,109,-10,2101,0,2,63,1008,63,30,63,1005,63,901,4,881,1001,64,1,64,1105,1,901,4,64,99,21102,1,27,1,21102,1,915,0,1106,0,922,21201,1,51805,1,204,1,99,109,3,1207,-2,3,63,1005,63,964,21201,-2,-1,1,21101,942,0,0,1106,0,922,22101,0,1,-1,21201,-2,-3,1,21101,0,957,0,1105,1,922,22201,1,-1,-2,1105,1,968,21201,-2,0,-2,109,-3,2105,1,0"""

intcode_list = real_data.split(",")
original_intcode_list = [int(x) for x in intcode_list]
print(intcode_computer(original_intcode_list, 2))


