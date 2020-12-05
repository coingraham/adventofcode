from aocd.models import Puzzle
puzzle = Puzzle(year=2020, day=5)

example = """BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL"""

bsp = puzzle.input_data.split("\n")
# bsp_example = example.split("\n")

seatid_list = []
for bsp in bsp:
    row = bsp[:-3].replace("F", "0").replace("B", "1")
    column = bsp[-3:].replace("L", "0").replace("R", "1")
    seatid_list.append((int(row, 2) * 8) + int(column, 2))

print(max(seatid_list))

for i, seat in enumerate(sorted(seatid_list)):
    if i + 51 != seat:
        print(seat - 1)
        break
