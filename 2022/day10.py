from aocd.models import Puzzle
puzzle = Puzzle(year=2022, day=10)

# Merry Christmas everyone!!!
# Always test with the sample input first!!
sample_input = '''addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop'''


# I eventually abandoned this code for a different approach.
def question1_alternate():
    question_input = sample_input

    x_register = 1
    cycles_that_matter = {20, 60, 100, 140, 180, 220}
    signal_strength = 0

    for cycle, signal in enumerate(question_input.splitlines()):

        if cycle * 2 in cycles_that_matter:
            print("Current cycle, register: {}, {}".format(cycle * 2, x_register))
            print("Current signal strength: {}".format(signal_strength))
            print("This cycle: {}\n".format(cycle * 2 * x_register))
            signal_strength += cycle * 2 * x_register

        if signal == "noop":
            continue

        number = int(signal.split(" ")[1])
        x_register += number

    print(signal_strength)


# Creating a new alternate question one using a different strategy.
def question1():
    # question_input = sample_input
    question_input = puzzle.input_data

    cycles_that_matter = {20, 60, 100, 140, 180, 220}
    signal_strength = 0
    memory = [1, ]

    # I decided to build a list of the commands and build in the cycles
    # that way I could take the sums collected on a slice of the array.
    for signal in question_input.splitlines():
        memory.append(0)

        # Noop only gets one cycle so break out of the process
        if signal == "noop":
            continue

        # Get the number and append to the memory list
        number = int(signal.split(" ")[1])
        memory.append(number)

    # Going through the cycles that matter and collecting sums
    for cycle in cycles_that_matter:
        signal_strength += cycle * sum(memory[0:cycle])

    print(signal_strength)


def question2():
    # question_input = sample_input
    question_input = puzzle.input_data

    memory = [1, ]

    # Using the same strategy as question 1, I create a list of the x_register commands
    # with all the cycle steps built in.
    for signal in question_input.splitlines():
        memory.append(0)

        if signal == "noop":
            continue

        number = int(signal.split(" ")[1])
        memory.append(number)

    x_register = 0
    crt = []

    # This loop breaks up my memory list into 40 unit chunks to process
    for crt_length in range(0, 240, 40):
        crt_row = []

        # I process each chunk of the crt in turn and add it to the crt collection
        for position, item in enumerate(memory[crt_length:crt_length + 40]):
            # Update the sprite position
            x_register += item

            # Check if the sprite is near our position and draw
            if abs(position - x_register) < 2:
                crt_row.append("#")
            else:
                crt_row.append(".")

        # Add each row of the crt back to the screen list
        crt.append(crt_row)

    # Display the answer
    for rows in crt:
        print(rows)


if __name__ == '__main__':
    # question1()
    question2()

