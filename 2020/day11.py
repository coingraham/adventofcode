from aocd.models import Puzzle
puzzle = Puzzle(year=2020, day=11)

example2 = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""

# seating_chart = [list(line) for line in example2.split("\n")]
seating_chart = [list(line) for line in puzzle.input_data.split("\n")]
max_x = len(seating_chart[0])
max_y = len(seating_chart)

# For this direction list, order matters.
# 0  1  2
# 3     4
# 5  6  7
# So that I can use enumerate to get both the "direction number" and the directional adjustment
direction_list = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]


def check_seat(x, y):
    surrounding_seats = []
    # Using range to get the 9 blocks in a 3x3 square
    for x_range in range(max(0, x - 1), min(max_x + 1, x + 2)):
        for y_range in range(max(0, y - 1), min(max_y + 1, y + 2)):
            # Exclude the middle square
            if x_range == x and y_range == y:
                continue
            try:
                # Collect all the neighboring seat information
                close_seat = seating_chart[y_range][x_range]
                surrounding_seats.append(close_seat)
            except IndexError:
                # I'd rather just catch the error than code the logic.
                continue

    # Check the surrounding seats against the rules and return
    if seat == "L" and surrounding_seats.count("#") == 0:
        return "#"
    elif seat == "#" and surrounding_seats.count("#") > 3:
        return "L"
    else:
        return seat


def check_seat_new_rules(x, y, this_seat):
    # If it's the ground return immediately
    if this_seat == ".":
        return this_seat

    # Loop over the 8 directions and look outward
    for direction_number, direction in enumerate(direction_list):
        # If another seat has seen us, we saw them and can skip
        if seat_view_tracker[(x, y)][direction_number] != ".":
            continue
        else:
            # Look this direction from the seat for anything interesting
            that_seat = look_this_direction(x, y, direction)
            if that_seat:
                # Save both seats to the tracker.
                # I'm using direction numbers like this:
                # 0  1  2
                # 3     4
                # 5  6  7
                # The opposites add up to 7 so if this seat looks
                # direction 2 (up right) the other seat will see it
                # on direction 5 (bottom left).  all the opposites add to 7.
                seat_view_tracker[that_seat[0]][7 - direction_number] = this_seat
                seat_view_tracker[(x, y)][direction_number] = that_seat[1]

    # Check the surrounding seats against the rules and return
    if this_seat == "L" and seat_view_tracker[(x, y)].count("#") == 0:
        return "#"
    elif this_seat == "#" and seat_view_tracker[(x, y)].count("#") > 4:
        return "L"
    else:
        return seat


def look_this_direction(x, y, direction):
    # Keep going a particular direction until we see something or fall off the boat
    while True:
        x += direction[0]
        y += direction[1]

        if x < 0 or x >= max_x or y < 0 or y >= max_y:
            return None
        else:
            if seating_chart[y][x] != ".":
                return (x, y), seating_chart[y][x]


def get_occupied(this_seating_chart):
    return sum([each_row.count("#") for each_row in this_seating_chart])


# This is the main part of the script
previous_count = 99999999
current_count = None
while True:
    # Build a dict for every point with an array of the 8 values around it.  This is my cache.
    seat_view_tracker = {(i, j): ["." for k in range(8)] for i in range(max_x) for j in range(max_y) if seating_chart[j][i] != "."}

    # Start with a blank new seating chart to fill in
    updated_seating_chart = [["." for columns in range(len(seating_chart[0]))] for rows in range(len(seating_chart))]
    for y, row in enumerate(seating_chart):
        for x, seat in enumerate(row):
            # updated_seating_chart[y][x] = check_seat(x, y)  # Part 1
            updated_seating_chart[y][x] = check_seat_new_rules(x, y, seat)  # Part 2

    # Finished updating the seating chart, get the count and compare
    current_count = get_occupied(updated_seating_chart)
    if current_count == previous_count:
        break
    else:
        previous_count = current_count
        current_count = None

    # Save the new chart and keep going
    seating_chart = updated_seating_chart.copy()

print(current_count)
