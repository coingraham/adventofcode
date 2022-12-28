from aocd.models import Puzzle

puzzle = Puzzle(year=2022, day=22)

# Merry Christmas everyone!!!
# Always test with the sample input first!!
sample_input = '''        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5'''

cube_size = 50

movement = {
    "up": -1j,
    "down": 1j,
    "right": 1,
    "left": -1
}

turning = {
    "right": {"L": "up", "R": "down"},
    "down": {"L": "right", "R": "left"},
    "left": {"L": "down", "R": "up"},
    "up": {"L": "left", "R": "right"},
}

facing_value = {
    "right": 0,
    "down": 1,
    "left": 2,
    "up": 3,
}

flip = {
    1: {
        "right": [2, "right"],
        "down": [3, "down"],
        "left": [4, "right"],
        "up": [6, "right"],
    },
    2: {
        "right": [5, "left"],
        "down": [3, "left"],
        "left": [1, "left"],
        "up": [6, "up"],
    },
    3: {
        "right": [2, "up"],
        "down": [5, "down"],
        "left": [4, "down"],
        "up": [1, "up"],
    },
    4: {
        "right": [5, "right"],
        "down": [6, "down"],
        "left": [1, "right"],
        "up": [3, "right"],
    },
    5: {
        "right": [2, "left"],
        "down": [6, "left"],
        "left": [4, "left"],
        "up": [3, "up"],
    },
    6: {
        "right": [5, "up"],
        "down": [2, "down"],
        "left": [1, "down"],
        "up": [4, "up"],
    },
}


def build_map_and_directions(question_input):
    all_input = question_input.splitlines()
    map_strings = all_input[:-2]
    directions_string = all_input[-1]

    # directions first
    directions = []
    temp_number = ""
    for char in [*directions_string]:
        if char in ["L", "R"]:
            directions.append(int(temp_number))
            directions.append(char)
            temp_number = ""
        else:
            temp_number = "{}{}".format(temp_number, char)
    else:
        directions.append(int(temp_number))

    # build map
    map_stuff = [[char for char in [*line]] for line in map_strings]

    # Get the widest rows to extend the others
    widest = max([len(row) for row in map_stuff])

    for row in map_stuff:
        if len(row) < widest:
            row.extend([" " for x in range(widest - len(row))])

    # Get the starting X point
    start_x = map_stuff[0].index(".")

    # Build a complex list of map values
    map_points = {}
    space_points = {}
    wall_points = {}
    for j, row in enumerate(map_stuff):
        for i, column in enumerate(row):
            if column == "#":
                wall_points[complex(i, j)] = column
                map_points[complex(i, j)] = column

            if column == ".":
                map_points[complex(i, j)] = column

            if column == " ":
                space_points[complex(i, j)] = column

    return map_stuff, map_points, space_points, wall_points, complex(start_x, 0), directions


def build_cube_and_directions(question_input):
    all_input = question_input.splitlines()
    map_strings = all_input[:-2]
    directions_string = all_input[-1]

    # directions first
    directions = []
    temp_number = ""
    for char in [*directions_string]:
        if char in ["L", "R"]:
            directions.append(int(temp_number))
            directions.append(char)
            temp_number = ""
        else:
            temp_number = "{}{}".format(temp_number, char)
    else:
        directions.append(int(temp_number))

    # build map
    map_stuff = [[char for char in [*line]] for line in map_strings]

    # Get the widest rows to extend the others
    widest = max([len(row) for row in map_stuff])

    for row in map_stuff:
        if len(row) < widest:
            row.extend([" " for x in range(widest - len(row))])

    # Build out the cube walls
    cube = {1: []}
    for y in range(0, cube_size):
        cube[1].append(map_stuff[y][cube_size: cube_size * 2])

    cube[2] = []
    for y in range(0, cube_size):
        cube[2].append(map_stuff[y][cube_size * 2: cube_size * 3])

    cube[3] = []
    for y in range(cube_size, cube_size * 2):
        cube[3].append(map_stuff[y][cube_size: cube_size * 2])

    cube[4] = []
    for y in range(cube_size * 2, cube_size * 3):
        cube[4].append(map_stuff[y][0: cube_size])

    cube[5] = []
    for y in range(cube_size * 2, cube_size * 3):
        cube[5].append(map_stuff[y][cube_size: cube_size * 2])

    cube[6] = []
    for y in range(cube_size * 3, cube_size * 4):
        cube[6].append(map_stuff[y][0: cube_size])

    return cube, complex(0, 0), directions


def get_map_result_by_point(point, map_input):
    new_x = int(point.real)
    new_y = int(point.imag)

    return map_input[new_y][new_x]


def check_next_step(point, map_input, facing, map_points, space_points):
    # Get x and y
    x = int(point.real)
    y = int(point.imag)

    # Fetch maximums for checking later
    max_x = len(map_input[0]) - 1
    max_y = len(map_input) - 1

    if facing == "right":
        if x > max_x or complex(x, y) in space_points:
            # Start from the left and find the first spot
            for this_x in range(max_x):
                if complex(this_x, y) in map_points:
                    return complex(this_x, y)
        else:
            return complex(x, y)

    if facing == "up":
        if y < 0 or complex(x, y) in space_points:
            # Start from the bottom and find the first spot
            for this_y in range(max_y, 0, -1):
                if complex(x, this_y) in map_points:
                    return complex(x, this_y)
        else:
            return complex(x, y)

    if facing == "left":
        if x < 0 or complex(x, y) in space_points:
            # Start from the right and find the first spot
            for this_x in range(max_x, 0, -1):
                if complex(this_x, y) in map_points:
                    return complex(this_x, y)
        else:
            return complex(x, y)

    if facing == "down":
        if y > max_y or complex(x, y) in space_points:
            # Start from the top and find the first spot
            for this_y in range(max_y):
                if complex(x, this_y) in map_points:
                    return complex(x, this_y)
        else:
            return complex(x, y)


def point_of_rotation(point, old_facing, new_facing):
    # Get x and y
    x = int(point.real)
    y = int(point.imag)

    cube_max = cube_size - 1

    if old_facing == "up" and new_facing == "up":
        return complex(x, cube_max)

    if old_facing == "up" and new_facing == "down":
        return complex(cube_max - x, 0)

    if old_facing == "up" and new_facing == "left":
        return complex(cube_max, cube_max - x)

    if old_facing == "up" and new_facing == "right":
        return complex(0, x)

    if old_facing == "up" and new_facing == "right":
        return complex(0, x)

    if old_facing == "down" and new_facing == "up":
        return complex(cube_max - x, cube_max)

    if old_facing == "down" and new_facing == "down":
        return complex(x, 0)

    if old_facing == "down" and new_facing == "right":
        return complex(0, cube_max - x)

    if old_facing == "down" and new_facing == "left":
        return complex(cube_max, x)

    if old_facing == "left" and new_facing == "up":
        return complex(cube_max - y, cube_max)

    if old_facing == "left" and new_facing == "left":
        return complex(cube_max, y)

    if old_facing == "left" and new_facing == "down":
        return complex(y, 0)

    if old_facing == "left" and new_facing == "right":
        return complex(0, cube_max - y)

    if old_facing == "right" and new_facing == "right":
        return complex(0, y)

    if old_facing == "right" and new_facing == "left":
        return complex(cube_max, cube_max - y)

    if old_facing == "right" and new_facing == "down":
        return complex(cube_max - y, 0)

    if old_facing == "right" and new_facing == "up":
        return complex(y, cube_max)

    print("Ruh roh!")


def check_next_cube(point, side, facing):
    # Get x and y
    x = int(point.real)
    y = int(point.imag)

    cube_max = cube_size - 1

    if 0 <= x <= cube_max and 0 <= y <= cube_max:
        return side, facing, complex(x, y)
    else:
        new_side, new_facing = flip[side][facing]
        return new_side, new_facing, point_of_rotation(point, facing, new_facing)


def question1():
    # question_input = sample_input
    question_input = puzzle.input_data

    # Setup the initial facing and get the input built
    facing = "right"
    map_input, map_points, space_points, wall_points, point, directions = build_map_and_directions(question_input)

    # Fetch maximums for checking later
    max_x = len(map_input[0])
    max_y = len(map_input)

    # Move or turn
    for counter, direction in enumerate(directions):
        if isinstance(direction, int):
            # Move the amount until you hit a wall
            for move in range(direction):
                # This is the potential next step.  I need to check it first.
                new_point = point + movement[facing]

                # Check if I need to loop around.  This is complicated so I'm going to write a
                # function for this.  Send in the point and the facing.
                new_point = check_next_step(new_point, map_input, facing, map_points, space_points)

                # Check if I hit a wall
                if new_point in wall_points:
                    break
                else:
                    point = new_point
        else:
            # Turn using the turning dictionary
            facing = turning[facing][direction]

    final_row = int(point.imag) + 1
    final_column = int(point.real) + 1

    print((1000 * final_row) + (4 * final_column) + facing_value[facing])


def question2():
    # The sample input is a different shape than the puzzle.  This will only work for the puzzle.
    question_input = puzzle.input_data

    # Setup the initial facing and get the input built
    facing = "right"
    side = 1
    cube, point, directions = build_cube_and_directions(question_input)

    # Move or turn
    for counter, direction in enumerate(directions):
        if isinstance(direction, int):
            # Move the amount until you hit a wall
            for move in range(direction):
                # This is the potential next step.  I need to check it first.
                new_point = point + movement[facing]

                # Check if I need to loop around.  This is complicated so I'm going to write a
                # function for this.  Send in the point and the facing.
                # new_point = check_next_step(new_point, map_input, facing, map_points, space_points)
                new_side, new_facing, new_point = check_next_cube(new_point, side, facing)

                # Check if I hit a wall
                if cube[new_side][int(new_point.imag)][int(new_point.real)] == "#":
                    break
                else:
                    point = new_point
                    facing = new_facing
                    side = new_side
        else:
            # Turn using the turning dictionary
            facing = turning[facing][direction]

    # Had to print out my point then hard code the adjustments from 0, 0
    print(point, side, facing)
    final_row = int(point.imag) + cube_size + 1
    final_column = int(point.real) + cube_size + 1

    # Not the prettiest but I got the solution
    print((1000 * final_row) + (4 * final_column) + facing_value[facing])


if __name__ == '__main__':
    # question1()
    question2()
