from aocd.models import Puzzle

puzzle = Puzzle(year=2025, day=5)

sample_data = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""

# question input
# q_i = [n for n in sample_data.splitlines()]
q_i = [n for n in puzzle.input_data.splitlines()]


def part_one():
    # split into ranges and ingredients
    seperator = q_i.index("")
    ranges = q_i[:seperator]
    ingredients = q_i[seperator+1:]

    # convert ranges to tuples
    ranges = [(int(r.split("-")[0]), int(r.split("-")[1])) for r in ranges]

    # convert ingredients to integers
    ingredients = [int(i) for i in ingredients]

    # fresh list
    fresh = []

    for ingredient in ingredients:
        for r in ranges:
            if r[0] <= ingredient <= r[1]:
                fresh.append(ingredient)
                break

    return len(fresh)
                

def part_two():
    # sample answer is 14
    total_range = 0
    
    # split into ranges and ingredients
    seperator = q_i.index("")
    ranges = q_i[:seperator]

    # convert ranges to tuples
    ranges = [(int(r.split("-")[0]), int(r.split("-")[1])) for r in ranges]

    # sort the ranges by the first value
    ranges.sort(key=lambda x: x[0])

    processing = True
    while processing:
        ranges, processing = check_ranges(ranges)

    for item in ranges:
        total_range += item[1] - item[0] + 1

    return total_range

def check_ranges(ranges):
    for i, r1 in enumerate(ranges):
        for j, r2 in enumerate(ranges):
            if i >= j:
                continue

            if r1[0] <= r2[0] <= r1[1] or r1[0] <= r2[1] <= r1[1]:
                ranges[i] = (min(r1[0], r2[0]), max(r1[1], r2[1]))
                ranges.remove(r2)
                return ranges, True

    return ranges, False


if __name__ == '__main__':
    # print(part_one())
    print(part_two())
