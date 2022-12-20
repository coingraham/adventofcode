from aocd.models import Puzzle
puzzle = Puzzle(year=2022, day=18)

# Merry Christmas everyone!!!
# Always test with the sample input first!!
sample_input = '''2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5'''

alternate_sample = '''1,1,1
2,1,1
3,1,1
4,1,1
5,1,1
6,1,1
1,2,1
2,2,1
4,2,1
5,2,1
6,2,1
1,3,1
2,3,1
3,3,1
4,3,1
5,3,1
6,3,1
1,4,1
2,4,1
3,4,1
4,4,1
5,4,1
6,4,1
1,1,2
2,1,2
3,1,2
4,1,2
5,1,2
6,1,2
1,2,2
6,2,2
1,3,2
6,3,2
1,4,2
2,4,2
3,4,2
4,4,2
5,4,2
6,4,2
1,1,3
2,1,3
3,1,3
4,1,3
5,1,3
6,1,3
1,2,3
2,2,3
3,2,3
4,2,3
5,2,3
6,2,3
1,3,3
2,3,3
3,3,3
4,3,3
5,3,3
6,3,3
1,4,3
2,4,3
3,4,3
4,4,3
5,4,3
6,4,3
1,1,4
2,1,4
3,1,4
4,1,4
5,1,4
6,1,4
1,2,4
6,2,4
1,3,4
6,3,4
1,4,4
2,4,4
3,4,4
4,4,4
5,4,4
6,4,4
1,1,5
2,1,5
3,1,5
4,1,5
5,1,5
6,1,5
1,2,5
2,2,5
3,2,5
4,2,5
5,2,5
6,2,5
1,3,5
2,3,5
3,3,5
4,3,5
5,3,5
6,3,5
1,4,5
2,4,5
3,4,5
4,4,5
5,4,5
6,4,5'''


def check_for_connected(point, point_map):
    side_count = 6
    x = point[0]
    y = point[1]
    z = point[2]

    # Check x
    if "{}_{}_{}".format(x - 1, y, z) in point_map:
        side_count -= 1

    if "{}_{}_{}".format(x + 1, y, z) in point_map:
        side_count -= 1

    # Check y
    if "{}_{}_{}".format(x, y - 1, z) in point_map:
        side_count -= 1

    if "{}_{}_{}".format(x, y + 1, z) in point_map:
        side_count -= 1

    # Check z
    if "{}_{}_{}".format(x, y, z - 1) in point_map:
        side_count -= 1

    if "{}_{}_{}".format(x, y, z + 1) in point_map:
        side_count -= 1

    return side_count


# Part 2: Checking the 6 sides of every point for other cubes and air pockets
def check_for_connected_excluding_air(point, point_map, air_list):
    side_count = 6
    x = point[0]
    y = point[1]
    z = point[2]

    # Check x axis for other cubes and air pockets
    if "{}_{}_{}".format(x - 1, y, z) in point_map or (x - 1, y, z) in air_list:
        side_count -= 1

    if "{}_{}_{}".format(x + 1, y, z) in point_map or (x + 1, y, z) in air_list:
        side_count -= 1

    # Check y axis for other cubes and air pockets
    if "{}_{}_{}".format(x, y - 1, z) in point_map or (x, y - 1, z) in air_list:
        side_count -= 1

    if "{}_{}_{}".format(x, y + 1, z) in point_map or (x, y + 1, z) in air_list:
        side_count -= 1

    # Check z axis for other cubes and air pockets
    if "{}_{}_{}".format(x, y, z - 1) in point_map or (x, y, z - 1) in air_list:
        side_count -= 1

    if "{}_{}_{}".format(x, y, z + 1) in point_map or (x, y, z + 1) in air_list:
        side_count -= 1

    # All that's left should be exposed sides
    return side_count


# Part 2: Finding the air pockets so we exclude them later
def find_air_pockets(points):

    # Potential air pockets groupings
    xy = {}
    xz = {}
    yz = {}

    # We're looking for air pockets in all three dimensions
    air_pocket_scores = {}

    # We log each point into the lists for review later
    for point in points:
        x = point[0]
        y = point[1]
        z = point[2]
        xyk = "{}_{}".format(x, y)
        xzk = "{}_{}".format(x, z)
        yzk = "{}_{}".format(y, z)

        # Building the dictionaries.  I wish Python would allow you to assign before check.
        if xyk not in xy:
            xy[xyk] = [z]
        else:
            xy[xyk].append(z)

        if xzk not in xz:
            xz[xzk] = [y]
        else:
            xz[xzk].append(y)

        if yzk not in yz:
            yz[yzk] = [x]
        else:
            yz[yzk].append(x)

    # Now we go through each sets of lists and determine what the air pockets might be.
    for k, v in xy.items():
        # Ignore the individuals
        if len(v) == 1:
            continue
        else:
            x, y = k.split("_")
            v = sorted(v)
            for num in range(v[0], v[-1] + 1):
                if num not in v:
                    aps_key = "{}_{}_{}".format(x, y, num)
                    if aps_key not in air_pocket_scores:
                        air_pocket_scores[aps_key] = 1
                    else:
                        air_pocket_scores[aps_key] += 1

    # We go through the second set of values
    for k, v in xz.items():
        if len(v) == 1:
            continue
        else:
            x, z = k.split("_")
            v = sorted(v)
            for num in range(v[0], v[-1] + 1):
                if num not in v:
                    aps_key = "{}_{}_{}".format(x, num, z)
                    if aps_key not in air_pocket_scores:
                        air_pocket_scores[aps_key] = 1
                    else:
                        air_pocket_scores[aps_key] += 1

    # Review the last set of values
    for k, v in yz.items():
        if len(v) == 1:
            continue
        else:
            y, z = k.split("_")
            v = sorted(v)
            for num in range(v[0], v[-1] + 1):
                if num not in v:
                    aps_key = "{}_{}_{}".format(num, y, z)
                    if aps_key not in air_pocket_scores:
                        air_pocket_scores[aps_key] = 1
                    else:
                        air_pocket_scores[aps_key] += 1

    # If a point has a value of 3, it's inside the droplet
    air_pocket_keys = [k for k, v in air_pocket_scores.items() if v == 3]

    # Convert from the text string to a list of tuples
    air_pocket_list = [(int(element.split("_")[0]),
                        int(element.split("_")[1]),
                        int(element.split("_")[2])) for element in air_pocket_keys]

    return air_pocket_list


def question1():
    # question_input = sample_input
    question_input = alternate_sample
    # question_input = puzzle.input_data

    points = [(int(element.split(",")[0]), int(element.split(",")[1]), int(element.split(",")[2]))
              for element in question_input.splitlines()]

    # Build a points map for easy comparison
    point_map = {}
    for point in points:
        point_key = "{}_{}_{}".format(point[0], point[1], point[2])
        point_map[point_key] = 0

    exposed_sides = 0
    for point in points:
        point_sides = check_for_connected(point, point_map)
        exposed_sides += point_sides

    print(exposed_sides)


def question2():
    # question_input = sample_input
    question_input = alternate_sample
    # question_input = puzzle.input_data

    points = [(int(element.split(",")[0]), int(element.split(",")[1]), int(element.split(",")[2]))
              for element in question_input.splitlines()]

    # Build a points map for easy comparison
    point_map = {}
    for point in points:
        point_key = "{}_{}_{}".format(point[0], point[1], point[2])
        point_map[point_key] = 0

    air_pocket_list = find_air_pockets(points)

    exposed_sides = 0
    for point in points:
        point_sides = check_for_connected_excluding_air(point, point_map, air_pocket_list)
        exposed_sides += point_sides

    print(exposed_sides)


if __name__ == '__main__':
    # question1()
    question2()

