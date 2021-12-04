from aocd.models import Puzzle
puzzle = Puzzle(year=2020, day=14)

example = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""

# init_program = [item.split(" = ") for item in example.split("\n")]
init_program = [item.split(" = ") for item in puzzle.input_data.split("\n")]

or_mask = None
and_mask = None
memory = {}
for line_parts in init_program:
    if line_parts[0] == "mask":
        or_mask = int(line_parts[1].replace("X", "0"), 2)
        and_mask = int(line_parts[1].replace("X", "1"), 2)

    else:
        mem = int(line_parts[0][4:-1])
        # bin_version = list("{:036b}".format(int(line_parts[1])))
        binary = int(line_parts[1])
        binary = binary & and_mask
        binary = binary | or_mask

        memory[mem] = int(binary)

answer = sum([total for total in memory.values()])
print(answer)
