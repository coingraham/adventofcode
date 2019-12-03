import aoc_common as ac
from aocd.models import Puzzle

puzzle = Puzzle(year=2019, day=3)

wires = puzzle.input_data.splitlines()
wire1_directive = wires[0]
wire2_directive = wires[1]

wire1 = [[0, 0]]
for directive in wire1_directive.split(","):
    direction = directive[0:1]
    amount = int(directive[1:])
    wire1 = ac.build_wire(wire1, direction, amount)

# wire2 = [0,0]
# intersection = []
# for directive in wire2_directive.split(","):
#     direction = directive[0:1]
#     amount = int(directive[1:])
#     wire2, intersection = ac.build_intersection_wire(wire2, wire1, direction, amount, intersection)

wire2 = [[0, 0]]
for directive in wire2_directive.split(","):
    direction = directive[0:1]
    amount = int(directive[1:])
    wire2 = ac.build_wire(wire2, direction, amount)

# print(wire1)
# print(wire2)

closest = 10000000000000
closest_point = None

intersection1 = [[-982, -845], [-967, -1254], [-649, -1400], [31, -1400], [31, -1644], [31, -1505], [543, -1505], [711, -2188], [660, -2188], [63, -2586], [-261, -2895], [-261, -2838], [116, -2838], [-649, -1763], [-967, -1497], [-1446, -1497], [-1518, -945], [-1518, -845], [-2054, -786], [-2530, -1074], [-2680, -1074], [-2723, -1260], [-2723, -1838], [-2723, -1889], [-2081, -1903], [-1716, -1210], [-1446, -1210], [-1060, -1562], [-1446, -1599], [-1707, -1562], [-1716, -996], [-2120, -996], [-2367, -1043], [-2505, -1889], [-2368, -2541], [-649, -1259], [-967, -1259], [-1058, -845], [-967, -910], [-967, -1302], [-649, -1302], [-602, -946], [113, -894], [1000, -517], [1000, -502], [1000, -226], [860, 0], [1000, -239], [931, 0]]

# for item in intersection1:
#     current_distance = ac.get_manhattan_closest([0, 0], item)
#     if current_distance < closest:
#         closest = current_distance
#         closest_point = item
#
# print(closest_point)
# print(closest)
# puzzle.answer_a = closest

lowest_steps = 10000000000000

for item in intersection1:
    wire1_steps = wire1.index(item)
    wire2_steps = wire2.index(item)
    steps = wire1_steps + wire2_steps

    if steps < lowest_steps:
        lowest_steps = steps

print(lowest_steps)
puzzle.answer_b = lowest_steps
