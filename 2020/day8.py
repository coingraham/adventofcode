from aocd.models import Puzzle
puzzle = Puzzle(year=2020, day=8)

example = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""

raw_game_code = puzzle.input_data.split("\n")
# game_code = example.split("\n")

game_code = []
for commands in raw_game_code:
    command, values = commands.split(" ")
    game_code.append((command, values))


def run_the_game(game_code):
    executed = []
    line = 0
    accumulator = 0
    while True:
        try:
            executed.append(line)
            if game_code[line][0].startswith("nop"):
                line += 1

            elif game_code[line][0].startswith("acc"):
                if game_code[line][1][0] == "+":
                    accumulator += int(game_code[line][1][1:])
                else:
                    accumulator -= int(game_code[line][1][1:])
                line += 1

            elif game_code[line][0].startswith("jmp"):
                if game_code[line][1][0] == "+":
                    line += int(game_code[line][1][1:])
                else:
                    line -= int(game_code[line][1][1:])
            if line in executed:
                return False, accumulator

        except IndexError as e:
            return True, accumulator

print(run_the_game(game_code))

for entry in range(len(game_code)):
    dev_code = game_code.copy()
    if dev_code[entry][0].startswith("jmp"):
        dev_code[entry] = ("nop", dev_code[entry][1])
        results = run_the_game(dev_code)
        if results[0]:
            print(results)

    elif dev_code[entry][0].startswith("nop"):
        dev_code[entry] = ("jmp", dev_code[entry][1])
        results = run_the_game(dev_code)
        if results[0]:
            print(results)