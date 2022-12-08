from aocd.models import Puzzle
from pprint import pprint

puzzle = Puzzle(year=2022, day=8)

# Merry Christmas everyone!!!
# Always test with the sample input first!!
sample_input = '''30373
25512
65332
33549
35390'''


def build_tree_map(tree_input):
    tree_map = []

    for tree_line in tree_input.splitlines():
        # This splits the string numbers into a numbered list
        tree_line_numbers = [int(tree_line[t: t + 1]) for t in range(0, len(tree_line))]
        # Add each to the two dimensional list
        tree_map.append(tree_line_numbers)

    return tree_map


def question1():
    # question_input = sample_input
    question_input = puzzle.input_data

    # Build a map of the tree heights
    tree_map = build_tree_map(question_input)

    width = len(tree_map[0])
    height = len(tree_map)
    current_tree = None
    seen_list = {}

    # Check from the left and right
    for row in range(1, height - 1):
        for column in range(width):
            # First tree sets the height and ups the count
            if column == 0:
                current_tree = tree_map[row][column]
                coordinates = "{}_{}".format(row, column)
                if coordinates in seen_list:
                    seen_list[coordinates] += 1
                else:
                    seen_list[coordinates] = 1
            else:
                if tree_map[row][column] > current_tree:
                    current_tree = tree_map[row][column]
                    coordinates = "{}_{}".format(row, column)
                    if coordinates in seen_list:
                        seen_list[coordinates] += 1
                    else:
                        seen_list[coordinates] = 1

        for column in reversed(range(width)):
            # First tree sets the height and ups the count
            if column == width - 1:
                current_tree = tree_map[row][column]
                coordinates = "{}_{}".format(row, column)
                if coordinates in seen_list:
                    seen_list[coordinates] += 1
                else:
                    seen_list[coordinates] = 1
            else:
                if tree_map[row][column] > current_tree:
                    current_tree = tree_map[row][column]
                    coordinates = "{}_{}".format(row, column)
                    if coordinates in seen_list:
                        seen_list[coordinates] += 1
                    else:
                        seen_list[coordinates] = 1

    # Check from up and down
    for column in range(1, width - 1):
        for row in range(height):
            # First tree sets the height and ups the count
            if row == 0:
                current_tree = tree_map[row][column]
                coordinates = "{}_{}".format(row, column)
                if coordinates in seen_list:
                    seen_list[coordinates] += 1
                else:
                    seen_list[coordinates] = 1
            else:
                if tree_map[row][column] > current_tree:
                    current_tree = tree_map[row][column]
                    coordinates = "{}_{}".format(row, column)
                    if coordinates in seen_list:
                        seen_list[coordinates] += 1
                    else:
                        seen_list[coordinates] = 1

        for row in reversed(range(height)):
            # First tree sets the height and ups the count
            if row == height - 1:
                current_tree = tree_map[row][column]
                coordinates = "{}_{}".format(row, column)
                if coordinates in seen_list:
                    seen_list[coordinates] += 1
                else:
                    seen_list[coordinates] = 1
            else:
                if tree_map[row][column] > current_tree:
                    current_tree = tree_map[row][column]
                    coordinates = "{}_{}".format(row, column)
                    if coordinates in seen_list:
                        seen_list[coordinates] += 1
                    else:
                        seen_list[coordinates] = 1

    # pprint(tree_map)
    # We never evaluate the four corners which are always seen.
    pprint(len(seen_list.keys()) + 4)


def question2():
    # question_input = sample_input
    question_input = puzzle.input_data

    # Build a map of the tree heights
    tree_map = build_tree_map(question_input)

    height = len(tree_map)
    width = len(tree_map[0])
    best_view = 0

    # Walk through the inside of the map and evaluate each tree one at a time
    # we can ignore the outside edge since they have a 0 side which would end
    # up being 0 when multiplied
    for row in range(1, width - 1):
        for column in range(1, height - 1):

            # print("Currently evaluating: {}, {}".format(row, column))
            current_tree = tree_map[row][column]

            # Walk up from our current position and check tree heights
            up = 0
            for check_up in range(row - 1, -1, -1):
                # print("up: {}, {}".format(check_up, column))
                if tree_map[check_up][column] < current_tree:
                    up += 1
                else:
                    up += 1
                    break

            # Walk down from our current position and check tree heights
            down = 0
            for check_down in range(row + 1, height):
                # print("down: {}, {}".format(check_down, column))
                if tree_map[check_down][column] < current_tree:
                    down += 1
                else:
                    down += 1
                    break

            # Walk right from our current position and check tree heights
            right = 0
            for check_right in range(column + 1, width):
                # print("right: {}, {}".format(row, check_right))
                if tree_map[row][check_right] < current_tree:
                    right += 1
                else:
                    right += 1
                    break

            # Walk left from our current position and check tree heights
            left = 0
            for check_left in range(column - 1, -1, -1):
                # print("left: {}, {}".format(row, check_left))
                if tree_map[row][check_left] < current_tree:
                    left += 1
                else:
                    left += 1
                    break

            # Calculate view by multiplying
            view = up * down * left * right
            # print("View score: {}".format(view))

            # Check against the current best view and save if better
            if view > best_view:
                best_view = view

    pprint(best_view)


if __name__ == '__main__':
    question1()
    question2()
