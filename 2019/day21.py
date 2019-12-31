import aoc_intcode as ac
import day21_input as d21


ram = [int(x) for x in d21.input_data.split(",")]
computer = ac.full_intcode_computer(ram, 0, 0, locals())
code = [
    # "NOT C J\n",
    # "AND A J\n",
    # "NOT A T\n",
    # "OR T J\n",
    # "NOT A J\n",
    # "NOT B T\n",
    # "AND T J\n",
    # "NOT C T\n",
    # "AND T J\n",
    # "AND D J\n",
    # "AND A T\n",
    # "AND C T\n",
    # "NOT T J\n",
    # "NOT D T\n",
    # "NOT T T\n",
    # "AND T J\n",
    "NOT A T\n",
    "NOT C J\n",
    "OR T J\n",
    "AND D J\n",
    "WALK\n"
]

code_ascii = []
for x in code:
    code_ascii.append([ord(y) for y in list(x)])

inputs = code_ascii.pop(0)

screen = []
while True:
    try:
        output = next(computer)
        if output == "Waiting for Input":
            print("".join(screen))
            inputs = code_ascii.pop(0)
        elif output == 10:
            print("".join(screen))
            screen = []
        else:
            screen.append(chr(output))
    except Exception as e:
        break


print(output)