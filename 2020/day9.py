from aocd.models import Puzzle
puzzle = Puzzle(year=2020, day=9)

example = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""

xmas_list = [int(x) for x in puzzle.input_data.split("\n")]
# xmas_list = [int(x) for x in example.split("\n")]

def walk_xmas(preamble):
    for item, tranche in enumerate([(xmas_list[x:x + preamble]) for x in range(0, len(xmas_list) - preamble)]):
        evaluate_me = xmas_list[item + preamble]
        found = False
        for number in tranche:
            if evaluate_me - number in tranche:
                found = True

        if found:
            continue
        else:
            return evaluate_me


def find_the_group(maximum, target):
    for size in range(2, maximum):
        for tranche in [(xmas_list[x:x + size]) for x in range(0, len(xmas_list) - size)]:
            if sum(tranche) == target:
                return min(tranche) + max(tranche)


invalid = walk_xmas(25)
invalid_position = xmas_list.index(invalid)
print("Here's invalid {} at position {}".format(invalid, invalid_position))

print(find_the_group(invalid_position, invalid))