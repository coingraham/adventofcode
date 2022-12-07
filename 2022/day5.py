from aocd.models import Puzzle
import re
puzzle = Puzzle(year=2022, day=5)

# Merry Christmas everyone!!!
# Always test with the sample input first!!
sample_input = '''    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2'''


def split_crates_moves(my_input):

    # Remove unnecessary characters, make it easier to format the input.
    splitlines = my_input.splitlines()

    # Find the line that divides crates from moves
    split_here = splitlines.index('')

    # Get the width of the crate piles
    width = int(splitlines[split_here - 1][-2])

    # Fill in the crate positions
    positions = []
    for pos, stack in enumerate(splitlines[split_here - 1]):
        if stack != " ":
            positions.append(pos)

    # Break up and format the crates
    # Instead of building the crates in stacks like the puzzle, I
    # lay the stacks on their side so it will be easy to manipulate them
    # as lists.
    crates_list = splitlines[:split_here - 1]
    crates = [[] for i in range(width)]
    for crate in list(reversed(crates_list)):
        for item in range(0, width):
            if crate[positions[item]] != " ":
                crates[item].append(crate[positions[item]])

    # Break up and format the moves
    moves_list = splitlines[split_here + 1:]
    moves = []
    for move in moves_list:
        moves.append([int(d) for d in move.split() if d.isdigit()])

    return crates, moves


def question1():
    question_input = sample_input
    # question_input = puzzle.input_data

    # Get the crates and moves
    crates, moves = split_crates_moves(question_input)

    # Loop through the movement activities and move stuff
    for move in moves:
        number_of_actions = move[0]
        source = move[1] - 1
        target = move[2] - 1

        for actions in range(number_of_actions):
            crate_to_move = crates[source].pop(-1)
            crates[target].append(crate_to_move)

    # Return the top crates
    top_crates = ""
    for crate in crates:
        top_crates += crate[-1]

    print(top_crates)


def question2():
    # question_input = sample_input
    question_input = puzzle.input_data

    # Get the crates and moves
    crates, moves = split_crates_moves(question_input)

    # Loop through the movement activities and move stuff
    for move in moves:
        number_of_actions = move[0]
        source = move[1] - 1
        target = move[2] - 1

        crate_to_move = []
        for actions in range(number_of_actions):
            crate_to_move.insert(0, crates[source].pop(-1))

        crates[target].extend(crate_to_move)

    # Return the top crates
    top_crates = ""
    for crate in crates:
        top_crates += crate[-1]

    print(top_crates)


if __name__ == '__main__':
    question1()
    question2()

