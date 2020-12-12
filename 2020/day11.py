from aocd.models import Puzzle
puzzle = Puzzle(year=2020, day=11)

from pprint import pprint

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
direction_list = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]


def check_seat(x, y):
    surrounding_seats = []
    for x_range in range(max(0, x - 1), min(max_x + 1, x + 2)):
        for y_range in range(max(0, y - 1), min(max_y + 1, y + 2)):
            if x_range == x and y_range == y:
                continue
            try:
                close_seat = seating_chart[y_range][x_range]
                surrounding_seats.append(close_seat)
            except IndexError:
                continue

    if seat == "L" and surrounding_seats.count("#") == 0:
        return "#"
    elif seat == "#" and surrounding_seats.count("#") > 3:
        return "L"
    else:
        return seat


def check_seat_new_rules(x, y, this_seat):
    if this_seat == ".":
        return this_seat

    # Loop over the 8 directions and look outward
    for direction_number, direction in enumerate(direction_list):
        if seat_view_tracker[(x, y)][direction_number] != ".":
            continue
        else:
            that_seat = look_this_direction(x, y, direction)
            if that_seat:
                seat_view_tracker[that_seat[0]][7 - direction_number] = this_seat
                seat_view_tracker[(x, y)][direction_number] = that_seat[1]

    if this_seat == "L" and seat_view_tracker[(x, y)].count("#") == 0:
        return "#"
    elif this_seat == "#" and seat_view_tracker[(x, y)].count("#") > 4:
        return "L"
    else:
        return seat


def look_this_direction(x, y, direction):
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


# pprint(seating_chart)
previous_count = 99999999
current_count = 0
while True:
    seat_view_tracker = {(i, j): ["." for k in range(8)] for i in range(max_x) for j in range(max_y) if seating_chart[j][i] != "."}
    updated_seating_chart = [["." for columns in range(len(seating_chart[0]))] for rows in range(len(seating_chart))]
    for y, row in enumerate(seating_chart):
        for x, seat in enumerate(row):
            # updated_seating_chart[y][x] = check_seat(x, y, seating_chart)  # Part 1
            updated_seating_chart[y][x] = check_seat_new_rules(x, y, seat)  # Part 2

    current_count = get_occupied(updated_seating_chart)
    if current_count == previous_count:
        break
    else:
        previous_count = current_count
        current_count = 0

    seating_chart = updated_seating_chart.copy()



print(current_count)