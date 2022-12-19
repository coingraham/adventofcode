from aocd.models import Puzzle
from time import sleep
import os
puzzle = Puzzle(year=2022, day=17)

# Merry Christmas everyone!!!
# Always test with the sample input first!!
sample_input = '''>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'''

piece1 = {
    "name": "-",
    "shape": [["#", "#", "#", "#"]],
    "left": [(0, 0)],
    "right": [(3, 0)],
    "down": [(0, 0), (1, 0), (2, 0), (3, 0)]
}

piece2 = {
    "name": "+",
    "shape": [[".", "#", "."], ["#", "#", "#"], [".", "#", "."]],
    "left": [(1, 0), (0, 1), (1, 2)],
    "right": [(1, 0), (2, 1), (1, 2)],
    "down": [(0, 1), (2, 1), (1, 0)]
}

piece3 = {
    "name": "_|",
    "shape": [["#", "#", "#"], [".", ".", "#"], [".", ".", "#"]],
    "left": [(0, 0), (2, 1), (2, 2)],
    "right": [(2, 0), (2, 1), (2, 2)],
    "down": [(0, 0), (1, 0), (2, 0)]
}

piece4 = {
    "name": "|",
    "shape": [["#"], ["#"], ["#"], ["#"]],
    "left": [(0, 0), (0, 1), (0, 2), (0, 3)],
    "right": [(0, 0), (0, 1), (0, 2), (0, 3)],
    "down": [(0, 0)]
}

piece5 = {
    "name": "box",
    "shape": [["#", "#"], ["#", "#"]],
    "left": [(0, 0), (0, 1)],
    "right": [(1, 0), (1, 1)],
    "down": [(0, 0), (1, 0)]
}

rocks = [piece1, piece2, piece3, piece4, piece5]


def build_move_list(question_input):
    # Did I really need a separate function for this?
    # interesting use of the "*" unpack command
    return [*question_input]


def expand_up(chamber, height):

    # Add a bunch of rows on top to extend.
    [chamber.append(["." for i in range(7)]) for level in range(height)]

    return chamber


def draw_the_rock_in_the_chamber(chamber, rock, position):

    for y in range(len(rock["shape"])):
        for x in range(len(rock["shape"][0])):
            if rock["shape"][y][x] == "#":
                chamber[y + position[1]][x + position[0]] = rock["shape"][y][x]

    return chamber


def show_the_chamber(chamber, rock, position):

    # Get the hashes
    rock_hashes = {}
    for y, row in enumerate(rock["shape"]):
        for x, column in enumerate(row):
            if column == "#":
                this = "{}_{}".format(x + position[0], y + position[1])
                rock_hashes[this] = "#"

    os.system('clear')
    for y in range(len(chamber) - 1, -1, -1):
        printable = "| "
        for x in range(0, len(chamber[0])):
            test = "{}_{}".format(x, y)
            if test in rock_hashes:
                printable += "# "
            else:
                printable += "{} ".format(chamber[y][x])

        printable += " |"
        print(printable)

    print("\n")


def get_current_height(chamber):

    for num, line in enumerate(chamber):
        if num == 0:
            continue

        if "#" not in line:
            return 2, num + 3


def question1():
    # question_input = sample_input
    question_input = puzzle.input_data

    gas_list = build_move_list(question_input)

    highest_rock_height = 0
    rock_pos = (2, 4)

    chamber = [["-" for i in range(7)]]

    # Expand the chamber up to accommodate more pieces
    chamber = expand_up(chamber, 8)

    # Total rocks dropped and gas tracker are faux counters.
    total_rocks_dropped = 0
    gas_tracker = 0

    while True:
        if total_rocks_dropped == 2022:
            print(rock_pos[1] - 4)
            break

        # Let's drop a rock and use modulo to cycle the rocks
        rock = rocks[total_rocks_dropped % len(rocks)]

        # show_the_chamber(chamber, rock, rock_pos)
        # sleep(1)

        # Now that a new rock exists, we need to process the movement
        while rock:
            # Get gas action
            gas_action = gas_list[gas_tracker % len(gas_list)]
            gas_tracker += 1

            # Check for blockages
            if gas_action == "<":
                # Check left and move
                for leftest in rock["left"]:
                    check = (leftest[0] + rock_pos[0], leftest[1] + rock_pos[1])
                    if check[0] == 0 or chamber[check[1]][check[0] - 1] == "#":
                        break
                else:
                    rock_pos = (rock_pos[0] - 1, rock_pos[1])

                    # Let's sleep and draw the board
                    # show_the_chamber(chamber, rock, rock_pos)

            else:
                # Check right and move
                for rightest in rock["right"]:
                    check = (rightest[0] + rock_pos[0], rightest[1] + rock_pos[1])
                    if check[0] == 6 or chamber[check[1]][check[0] + 1] == "#":
                        break

                else:
                    rock_pos = (rock_pos[0] + 1, rock_pos[1])

                    # Let's sleep and draw the board
                    # show_the_chamber(chamber, rock, rock_pos)

            # Check down for resting and move down
            for downest in rock["down"]:
                check = (downest[0] + rock_pos[0], downest[1] + rock_pos[1])
                if check[1] == 1 or chamber[check[1] - 1][check[0]] == "#":
                    chamber = draw_the_rock_in_the_chamber(chamber, rock, rock_pos)
                    rock = None

                    # Set the current spawn point and expand the chamber
                    rock_pos = get_current_height(chamber)
                    chamber = expand_up(chamber, rock_pos[1] + 4 - len(chamber))

                    # Break out of the inner loop
                    break
            else:
                # Move the rock down a level
                rock_pos = (rock_pos[0], rock_pos[1] - 1)

                # Let's sleep and draw the board
                # show_the_chamber(chamber, rock, rock_pos)

        # Count the dropped rock
        total_rocks_dropped += 1


def question2():
    # question_input = sample_input
    question_input = puzzle.input_data

    gas_list = build_move_list(question_input)
    rock_pos = (2, 4)
    chamber = [["-" for i in range(7)]]

    # Expand the chamber up to accommodate more pieces
    chamber = expand_up(chamber, 8)

    # Total rocks dropped and gas tracker are faux counters.
    total_rocks_dropped = 0
    gas_tracker = 0
    max_rocks_dropped = 1_000_000_000_000
    # max_rocks_dropped = 2022

    # Variables to find the repeat and capture the amount
    total_rock_tracker = []
    total_height_tracker = []
    height_diff = []
    height_adjustment = 0
    rock_drop_adjustment = 0
    run_this = True

    while True:
        # Changed the final check to take the rock and height adjustments into account.
        if total_rocks_dropped == max_rocks_dropped - rock_drop_adjustment:
            print(height_adjustment + rock_pos[1] - 4)
            break

        # Let's drop a rock and use modulo to cycle the rocks
        rock = rocks[total_rocks_dropped % len(rocks)]

        # show_the_chamber(chamber, rock, rock_pos)

        # Now that a new rock exists, we need to process the movement
        while rock:

            # Basic itea here is that as the gas cycles back to the beginning, we will likely
            # start to see a pattern emerge.  We need to discover that pattern and use it to
            # fast-forward through the iterations.
            if gas_tracker % len(gas_list) == 0:
                # I put in a trigger, I only want to run the adjustment once
                if run_this:

                    # Tracking results and looking for patterns
                    total_rock_tracker.append(total_rocks_dropped)
                    total_height_tracker.append(rock_pos[1] - 4)

                    # I need to collect some results before I start comparing
                    if len(total_rock_tracker) > 4:

                        # Track the differences for comparison
                        this_tr_difference = total_rock_tracker[-1] - total_rock_tracker[-2]
                        this_hr_difference = total_height_tracker[-1] - total_height_tracker[-2]
                        height_diff.append(this_hr_difference)

                        tr_multiple = None
                        hr_multiple = None

                        # Collect some height differences
                        if len(height_diff) > 6:

                            # Look back through the differences for a pattern, collect all those values into
                            # an offset and track how many cycles.
                            offset = this_hr_difference
                            repeat = height_diff.pop(-1)
                            for num, element in enumerate(reversed(height_diff)):
                                if element != repeat:
                                    offset += element
                                else:
                                    tr_multiple = (num + 1) * this_tr_difference
                                    hr_multiple = offset
                                    break

                            # I've got the repeating cycles and now I adjust the rocks dropped and height
                            multiple = (max_rocks_dropped - total_rocks_dropped) // tr_multiple
                            rock_drop_adjustment = multiple * tr_multiple
                            height_adjustment = multiple * hr_multiple

                            # Stop this from running again.
                            run_this = False

            # THIS IS THE SAME AS BEFORE
            # Get gas action
            gas_action = gas_list[gas_tracker % len(gas_list)]
            gas_tracker += 1

            # Check for blockages
            if gas_action == "<":
                # Check left and move
                for leftest in rock["left"]:
                    check = (leftest[0] + rock_pos[0], leftest[1] + rock_pos[1])
                    if check[0] == 0 or chamber[check[1]][check[0] - 1] == "#":
                        break
                else:
                    rock_pos = (rock_pos[0] - 1, rock_pos[1])

                    # Let's draw the board
                    # show_the_chamber(chamber, rock, rock_pos)

            else:
                # Check right and move
                for rightest in rock["right"]:
                    check = (rightest[0] + rock_pos[0], rightest[1] + rock_pos[1])
                    if check[0] == 6 or chamber[check[1]][check[0] + 1] == "#":
                        break

                else:
                    rock_pos = (rock_pos[0] + 1, rock_pos[1])

                    # Let' draw the board
                    # show_the_chamber(chamber, rock, rock_pos)

            # Check down for resting and move down
            for downest in rock["down"]:
                check = (downest[0] + rock_pos[0], downest[1] + rock_pos[1])
                if check[1] == 1 or chamber[check[1] - 1][check[0]] == "#":
                    chamber = draw_the_rock_in_the_chamber(chamber, rock, rock_pos)
                    rock = None

                    # Set the current spawn point and expand the chamber
                    rock_pos = get_current_height(chamber)
                    chamber = expand_up(chamber, rock_pos[1] + 4 - len(chamber))

                    # Break out of the inner loop
                    break
            else:
                # Move the rock down a level
                rock_pos = (rock_pos[0], rock_pos[1] - 1)

                # Let's draw the board
                # show_the_chamber(chamber, rock, rock_pos)

        # Count the dropped rock
        total_rocks_dropped += 1


if __name__ == '__main__':
    # question1()
    question2()

