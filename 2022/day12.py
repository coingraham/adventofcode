from aocd.models import Puzzle
import string
from collections import deque
puzzle = Puzzle(year=2022, day=12)

# Merry Christmas everyone!!!
# Always test with the sample input first!!
sample_input = '''Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi'''


def build_map(map_input):

    my_map = []
    S = {}

    # Build a map of the inputs to be able to walk the paths to the destination
    map_input = list(reversed(map_input.splitlines()))
    for row_number, rows in enumerate(map_input):
        this_row = []
        for pos in range(len(rows)):
            letter = rows[pos]

            # Gather these special cases as we fill in the map
            if letter == "S":
                S = complex(pos, row_number)
                this_row.append("a")
                continue

            this_row.append(rows[pos])

        my_map.append(this_row)

    # We want to memoize where we've been so we can shortcut paths that loop back as
    # any path that touches a spot we've seen will automatically be longer than the
    # path that saw the point previously.
    memo = {}

    return my_map, S, memo


def get_letter_a_list(my_map):
    letter_a_list = []

    for y in range(len(my_map)):
        for x in range(len(my_map[0])):

            letter = my_map[y][x]
            if letter == "a":
                letter_a_list.append(complex(x, y))
                
    return letter_a_list


def get_steps(my_map, memo, point):
    paths = []
    height = len(my_map) - 1
    width = len(my_map[0]) - 1

    # Get up step
    up = point + 1j

    # Check if this step is outside the map
    if 0 <= int(up.real) <= width and 0 <= int(up.imag) <= height:
        up_point = "{}_{}".format(int(up.real), int(up.imag))

        # Check if we've stepped here before
        if up_point not in memo:
            paths.append(up)

    # Get down step
    down = point - 1j

    # Check if this step is outside the map
    if 0 <= int(down.real) <= width and 0 <= int(down.imag) <= height:
        down_point = "{}_{}".format(int(down.real), int(down.imag))

        # Check if we've stepped here before
        if down_point not in memo:
            paths.append(down)

    # Get right step
    right = point + 1

    # Check if this step is outside the map
    if 0 <= int(right.real) <= width and 0 <= int(right.imag) <= height:
        right_point = "{}_{}".format(int(right.real), int(right.imag))

        # Check if we've stepped here before
        if right_point not in memo:
            paths.append(right)

    # Get left step
    left = point - 1

    # Check if this step is outside the map
    if 0 <= int(left.real) <= width and 0 <= int(left.imag) <= height:
        left_point = "{}_{}".format(int(left.real), int(left.imag))

        # Check if we've stepped here before
        if left_point not in memo:
            paths.append(left)

    # Return the path options
    return paths


def get_shortest_path(my_map, memo, alphabet, S):

    # We're going to take a stack based approach to walking the paths for this map. We'll
    # pull the current path off the stack, check for path options, create new paths and put them
    # back on the stack to be evaluated later.
    stack = deque([[S]])

    while stack:

        # Each item on the stack will be a list of coordinates which will be the path walked, but
        # we're only interested in evaluating the last step of the path.
        this_path = stack.popleft()
        this_point = this_path[-1]
        this_letter = my_map[int(this_point.imag)][int(this_point.real)]
        this_path_point = "{}_{}".format(int(this_point.real), int(this_point.imag))

        # If we are visiting this spot for the first time, save it to the memo, otherwise
        # we can skip it.
        if this_path_point in memo:
            continue
        else:
            memo[this_path_point] = this_letter

        # E is the end.  If we've gotten here, return the steps in the path
        if this_letter == "E":
            answer_path = this_path.copy()
            return len(answer_path) - 1

        # Get all the possible paths, but not anything we've seen before
        paths = get_steps(my_map, memo, this_point)

        # Load the paths into the stack. This could create up to three new path options
        for path in paths:
            # Check the paths against the alphabet list.
            path_letter = my_map[int(path.imag)][int(path.real)]
            this_letter_index = alphabet.index(this_letter) + 2
            allowed_letters = alphabet[0:this_letter_index]
            if path_letter in allowed_letters:
                # Copy the list to keep from editing the original
                new_path = this_path.copy()
                new_path.append(path)
                stack.append(new_path)


def question1():
    # question_input = sample_input
    question_input = puzzle.input_data

    alphabet = list(string.ascii_lowercase)
    alphabet.insert(0, "S")
    alphabet.append("E")
    my_map, S, memo = build_map(question_input)

    print(get_shortest_path(my_map, memo, alphabet, S))


def question2():
    # question_input = sample_input
    question_input = puzzle.input_data

    shortest = []
    alphabet = list(string.ascii_lowercase)
    alphabet.append("E")
    my_map, S, memo = build_map(question_input)

    letter_a_list = get_letter_a_list(my_map)

    # Part 2: we check the original S first then we need to go through
    # the list of a's and switch S for each.
    for letter_a in letter_a_list:
        my_map, S, memo = build_map(question_input)
        S = letter_a
        pathway = get_shortest_path(my_map, memo, alphabet, S)
        if pathway is not None:
            shortest.append(pathway)

    print(min(shortest))


if __name__ == '__main__':
    question1()
    question2()
