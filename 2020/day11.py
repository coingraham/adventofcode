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

seating_chart = [list(line) for line in example2.split("\n")]
# seating_chart = [list(line) for line in puzzle.input_data.split("\n")]
max_x = len(seating_chart[0])
max_y = len(seating_chart)

direction_list = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
seat_view_tracker = {(i, j): ["." for k in range(8)] for i in range(max_x) for j in range(max_y) if seating_chart[j][i] != "."}

def check_seat(x, y, seat, new_seating_chart):
    surrounding_seats = []
    for x_range in range(max(0, x - 1), min(max_x + 1, x + 2)):
        for y_range in range(max(0, y - 1), min(max_y + 1, y + 2)):
            if x_range == x and y_range == y:
                continue
            try:
                close_seat = new_seating_chart[y_range][x_range]
                surrounding_seats.append(close_seat)
            except IndexError:
                continue

    if seat == "L" and surrounding_seats.count("#") == 0:
        return "#"
    elif seat == "#" and surrounding_seats.count("#") > 3:
        return "L"
    else:
        return seat


def check_seat_new_rules(x, y, seat, new_seating_chart):
    if seat == ".":
        return seat

    # Loop over the 8 directions and look outward
    for direction in direction_list:
        if seat_view_tracker[(x, y)][direction] != ".":
            pass




def get_occupied(this_seating_chart):
    return sum([each_row.count("#") for each_row in this_seating_chart])


# pprint(seating_chart)
previous_count = 99999999
current_count = 0
while True:

    updated_seating_chart = [["." for columns in range(len(seating_chart[0]))] for rows in range(len(seating_chart))]
    for y, row in enumerate(seating_chart):
        for x, seat in enumerate(row):
            # updated_seating_chart[y][x] = check_seat(x, y, seat, seating_chart)
            updated_seating_chart[y][x] = check_seat_new_rules(x, y, seat, seating_chart)

    current_count = get_occupied(updated_seating_chart)
    if current_count == previous_count:
        break
    else:
        previous_count = current_count
        current_count = 0

    seating_chart = updated_seating_chart.copy()

print(current_count)