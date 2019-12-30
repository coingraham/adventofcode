from itertools import combinations

import day25_input as d25
import aoc_intcode as ac


ram = [int(x) for x in d25.ram.split(",")]

cpu = ac.full_intcode_computer(ram, 0, 0, locals())


def get_output():
    output = []
    try:
        while True:
            this_output = next(cpu)
            if this_output == "Waiting for Input":
                # print("".join(chr(i) for i in output))
                return "".join(chr(i) for i in output)

            output.append(this_output)
            # if this_output == 10:
            #     print("".join(chr(i) for i in output))

    except Exception as e:
        print("".join(chr(i) for i in output))
        return output


action = {
    0: "north",
    1: "south",
    2: "east",
    3: "west",
    4: "take",
    5: "drop"
}

items = {
    0: "fixed point",
    1: "sand",
    2: "asterisk",
    3: "hypercube",
    4: "coin",
    5: "easter egg",
    6: "spool of cat6",
    7: "shell",
}

inputs = []
get_output()
commands = [
    [3],
    [4, 0],
    [0],
    [4, 1],
    [1],
    [2],
    [2],
    [4, 2],
    [0],
    [0],
    [4, 3],
    [0],
    [4, 4],
    [0],
    [4, 5],
    [1],
    [1],
    [1],
    [3],
    [0],
    [4, 6],
    [0],
    [4, 7],
    [3],
]
while commands:
    # x = input()
    this_command = commands.pop(0)
    if len(this_command) > 1:
        command = "{} {}{}".format(action[this_command[0]], items[this_command[1]], "\n")
    else:
        command = "{}{}".format(action[this_command[0]], "\n")
    inputs = [ord(y) for y in list(command)]
    get_output()


for tries in range(2, 8):
    for item_config in combinations('01234567', tries):
        for item in items.values():
            command = "{} {}{}".format("drop", item, "\n")
            inputs = [ord(y) for y in list(command)]
            get_output()

        command = "{}{}".format("inv", "\n")
        inputs = [ord(y) for y in list(command)]
        get_output()

        for pick_up in item_config:
            command = "{} {}{}".format("take", items[int(pick_up)], "\n")
            inputs = [ord(y) for y in list(command)]
            get_output()

        command = "{}{}".format("north", "\n")
        inputs = [ord(y) for y in list(command)]
        final = get_output()
        final = final.splitlines()

        if "ejected" in final[9].split(" "):
            print(final[9])
        else:
            print(item_config)

