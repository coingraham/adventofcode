from aocd.models import Puzzle
puzzle = Puzzle(year=2022, day=15)

# Merry Christmas everyone!!!
# Always test with the sample input first!!
sample_input = '''Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3'''


# Borrowed from AOC 2019
def get_manhattan_closest(coord1, coord2):
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])


def load_sensor_list(question_input):

    # I'm going to have a list of sensor tuples with the x, y, distance to the beacon.  I should be able to use
    # that to cover the important row.
    sensor_list = []
    beacon_list = []
    x_list = []
    y_list = []

    for sensor_reading in question_input.splitlines():
        sensor_split = sensor_reading.split(" ")
        x = sensor_split[2].split("=")[1].split(",")[0]
        sensor_x = int(sensor_split[2].split("=")[1].split(",")[0])
        sensor_y = int(sensor_split[3].split("=")[1].split(":")[0])
        beacon_x = int(sensor_split[8].split("=")[1].split(",")[0])
        beacon_y = int(sensor_split[9].split("=")[1].split(":")[0])

        distance = get_manhattan_closest((sensor_x, sensor_y), (beacon_x, beacon_y))

        x_list.append(sensor_x)
        x_list.append(beacon_x)
        y_list.append(sensor_y)
        y_list.append(beacon_y)

        sensor_data = (sensor_x, sensor_y, distance)
        sensor_list.append(sensor_data)
        beacon_list.append((beacon_x, beacon_y))

    return sensor_list, beacon_list, min(x_list), max(x_list), min(y_list), max(y_list)


def question1():
    question_input = sample_input
    # question_input = puzzle.input_data

    # Thinking about Part 1, do I actually need to build the map out?  Or can I just get the distance
    # for each sensor and mark the overlaps on the specific row?  Let's try it.

    # Sample looking at 10, real puzzle is 2_000_000
    important_row = 10
    # important_row = 2_000_000

    # I'm going to have a list of sensor tuples with the x, y, distance to the beacon.  I should be able to use
    # that to cover the important row.
    sensor_list, beacon_list, x_min, x_max, y_min, y_max = load_sensor_list(question_input)

    # Get the expected width of the row, it's probably not larger than two times the size of
    # the leftmost x from the rightmost x.
    width = (x_max - x_min) * 2
    # width = 3
    sensor_row = []

    new_min = x_min - width
    new_max = x_max + width

    for position in range(new_min, new_max):
        check_position = (position, important_row)

        # Check if this position is blocked by any of the sensors.  Just need to get
        # the distance and check if it's less than the beacon distance
        for sensor in sensor_list:
            this_distance = get_manhattan_closest((sensor[0], sensor[1]), check_position)
            if this_distance <= sensor[2]:
                sensor_row.append("#")
                break
        else:
            sensor_row.append(".")

    # Add the beacons into the list
    for beacon in beacon_list:
        if beacon[1] == important_row:
            sensor_row[beacon[0] + abs(new_min)] = "B"

    print(sensor_row.count("#"))


def question2():
    # question_input = sample_input
    question_input = puzzle.input_data

    # Max size sample 20, real puzzle is 4_000_000
    # max_search = 20
    max_search = 4_000_000

    # I'm going to have a list of sensor tuples with the x, y, distance to the beacon.
    sensor_list, beacon_list, x_min, x_max, y_min, y_max = load_sensor_list(question_input)
    sensor = None

    # Search through all the points for a coordinate that isn't covered by a sensor and
    # break out when you find it.
    for row in range(0, max_search + 1):

        # This is WAYYYYYYYY too slow.  It would have taken forever.
        # for column in range(0, max_search + 1):

        # Switched to this.  allows me to skip a bunch of cycles
        column = max_search
        while column:
            column -= 1

            check_position = (column, row)

            # Check if the coordinate is a beacon
            if check_position in beacon_list:
                continue

            # Efficiency:  Check the last sensor first
            if sensor:
                this_distance = get_manhattan_closest((sensor[0], sensor[1]), check_position)
                if this_distance <= sensor[2]:
                    column -= sensor[2] - this_distance
                    if column < 0:
                        column = 0
                    continue

            # Check if this position is blocked by any of the sensors.  Just need to get
            # the distance and check if it's less than the beacon distance
            for sensor in sensor_list:
                this_distance = get_manhattan_closest((sensor[0], sensor[1]), check_position)
                if this_distance <= sensor[2]:
                    column -= sensor[2] - this_distance
                    if column < 0:
                        column = 0
                    break
            else:
                results = (4_000_000 * check_position[0]) + check_position[1]
                print(results)

                # I'm using return to break out of the outer loop.  Python has no command
                # to break out of an outer loop.
                return results


if __name__ == '__main__':
    # question1()
    question2()

