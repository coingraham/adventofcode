example = """
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""

example_list = [list(x) for x in example.split()]

with open('test.in', mode='r') as f:
    puzzle_input = [list(x.strip()) for x in f.readlines()]


def tree_hitting_function(right, down, tree_input):
    # Get the height and width based on the list lengths
    height = len(tree_input)
    width = len(tree_input[0])

    # Set initial values
    trees = 0
    step = 0

    # Walk down the "hill" using range.
    for y in range(down, height, down):
        # We need to track steps down so we know how far to the right.
        step += 1

        # Modulo trick to cycle through the width values and loop back around to the front
        x_axis = (step * right) % width

        # Check if a tree and increment
        if tree_input[y][x_axis] == "#":
            trees += 1

    return trees


def slope_multiplier(slopes, tree_input):
    total = 1

    # Loop through the slopes and calc the trees hit.  Multiply them together.
    for slope in slopes:
        right = slope[0]
        down = slope[1]
        total *= tree_hitting_function(right, down, tree_input)

    return total


if __name__ == '__main__':
    print(tree_hitting_function(3, 1, puzzle_input))

    slope_list = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)
    ]

    print(slope_multiplier(slope_list, puzzle_input))
