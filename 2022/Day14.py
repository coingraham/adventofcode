from aocd.models import Puzzle
puzzle = Puzzle(year=2022, day=14)

# Merry Christmas everyone!!!
# Always test with the sample input first!!
sample_input = '''498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9'''


def build_wall_map(scanner_input):

    # Split the lines from the scanner
    scanner_lines = scanner_input.splitlines()

    # First I want to get the max values so I can build the map and
    # I get the min values for later
    x_list = set([])
    y_list = set([])
    coordinates_list = []
    for scanner_line in scanner_lines:
        coordinates = scanner_line.split(" -> ")
        coordinates_list.append(coordinates)
        for coord in coordinates:
            x, y = coord.split(",")
            x_list.add(int(x))
            y_list.add(int(y))

    min_x = min(x_list)
    min_y = min(y_list)
    max_x = max(x_list) + 1
    max_y = max(y_list) + 1

    # Part 2 needs the map to grow to the right, instead of discovering it, I just double the size
    # and hope for the best.
    wall_map = [["." for j in range(max_x * 2)] for i in range(max_y + 2)]
    wall_map[0][500] = "+"

    # Process each set of walls
    for coordinates in coordinates_list:
        # Pulling my tranche code from 2019.  This will create a window of items and step through the
        # list pulling out <size> groups.
        size = 2
        for tranche in [(coordinates[x:x + size]) for x in range(0, len(coordinates) - (size - 1), 1)]:
            # print(tranche)
            start_x, start_y = [int(i) for i in tranche[0].split(",")]
            stop_x, stop_y = [int(j) for j in tranche[1].split(",")]

            # Build the vertical walls
            if start_x == stop_x:
                # Step through each tranche of coordinates and build out the "#" walls
                for y in range(min(start_y, stop_y), max(start_y, stop_y) + 1):
                    wall_map[y][start_x] = "#"

            # Build the horizontal walls
            else:
                # Step through each tranche of coordinates and build out the "#" walls
                for x in range(min(start_x, stop_x), max(start_x, stop_x) + 1):
                    wall_map[start_y][x] = "#"

    # print_wall_map(wall_map, min_x, max_x, 0, max_y)

    return wall_map, min_x, max_x, min_y, max_y


def print_wall_map(wall_map, min_x, max_x, min_y, max_y):

    # Just print the interesting parts of the wall map
    for y in range(min_y, max_y + 2):
        print(wall_map[y][min_x: max_x])

    print("\n")


def drop_sand(wall_map):
    # Start at the drop point
    current_point = [500, 0]

    # Part 1:  I need the bottom of the map to know when it's done
    bottom_of_map = len(wall_map) - 1

    # Part 2: Check if the spout is closed
    if wall_map[current_point[1]][current_point[0]] == "O":
        return wall_map, 0

    # Loop through the movements and keep going
    while True:
        # Part 1: check if we've fallen to the last row.  That means we're done.
        if current_point[1] == bottom_of_map:
            return wall_map, 0

        # Try to go down.  In an upside down cartesian plan, down = (x, y + 1)
        if wall_map[current_point[1] + 1][current_point[0]] == ".":
            current_point = [current_point[0], current_point[1] + 1]
            continue

        # Try to go down and left.  In an upside down cartesian plan, down + left = (x - 1, y + 1)
        if wall_map[current_point[1] + 1][current_point[0] - 1] == ".":
            current_point = [current_point[0] - 1, current_point[1] + 1]
            continue

        # Try to go down and right.  In an upside down cartesian plan, down + rith = (x + 1, y + 1)
        if wall_map[current_point[1] + 1][current_point[0] + 1] == ".":
            current_point = [current_point[0] + 1, current_point[1] + 1]
            continue

        # Rest and save
        wall_map[current_point[1]][current_point[0]] = "O"

        # If we made it here, return the updated wall map and add one to the results.
        return wall_map, 1


def question1():
    question_input = sample_input
    # question_input = puzzle.input_data

    # Build the wall map
    wall_map, min_x, max_x, min_y, max_y = build_wall_map(question_input)

    # Set the resting sand variable
    resting_sand = 0

    # This will loop forever until we break out
    while True:
        # Drop the sand
        wall_map, adjustment = drop_sand(wall_map)

        # Print the map, this will help troubleshoot
        print_wall_map(wall_map, min_x, max_x, 0, max_y)

        # If the drop sand is 1, it is true, add one to the results
        if adjustment:
            resting_sand += 1
        else:
            # If the drop stand is 0, that's false, print the result and break
            print(resting_sand)
            break


def question2():
    question_input = sample_input
    # question_input = puzzle.input_data

    # Build the wall map
    wall_map, min_x, max_x, min_y, max_y = build_wall_map(question_input)

    # Part 2: Add the new floor
    floor = ["#" for i in wall_map[0]]
    wall_map[len(wall_map) - 1] = floor

    # Set the resting sand variable
    resting_sand = 0

    while True:
        # Drop the sand
        wall_map, adjustment = drop_sand(wall_map)

        # If the drop sand is 1, it is true, add one to the results
        if adjustment:
            resting_sand += 1
        else:
            # If the drop stand is 0, that's false, print the result and break
            print(resting_sand)
            # print_wall_map(wall_map, min_x - 160, max_x + 110, 0, max_y)
            break


if __name__ == '__main__':
    question1()
    question2()

