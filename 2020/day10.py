from math import prod
from itertools import combinations

from aocd.models import Puzzle
puzzle = Puzzle(year=2020, day=10)

example = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""

example2 = """16
10
15
5
1
11
7
19
6
12
4"""

adapters_list = sorted([int(x) for x in puzzle.input_data.split("\n")])
# adapters_list = sorted([int(x) for x in example.split("\n")])
adapters_list = sorted([int(x) for x in example2.split("\n")])
# adapters_list = sorted([int(x) for x in my_example.split("\n")])

# Add the start and end parts
adapters_list.insert(0, 0)
adapters_list.append(adapters_list[-1] + 3)

print(adapters_list)

joltage = [0, 0]
for number, adapter in enumerate(sorted(adapters_list)):

    if number == len(adapters_list) - 1:
        joltage[1] += 1
        print(joltage[0] * joltage[1])
        continue

    # print("adapter {}, adapter number {}, combined {}".format(adapter, number, adapters_list[number]))
    if adapters_list[number + 1] - adapter == 1:
        joltage[0] += 1
    elif adapters_list[number + 1] - adapter == 3:
        joltage[1] += 1


def get_combinations(number_list, size):
    list_length = len(number_list)
    if size == 0:
        return 1
    elif list_length - size > 1:
        return len(list(combinations(number_list, size)))

    return len(list(combinations(number_list, size))) + get_combinations(number_list, size - 1)


cache = {}
temp = []
for x in range(1, 4):
    temp.append(x)
    cache[x] = get_combinations(temp, x)


chunks = []
start_chunk = -1
for number, item in enumerate(sorted(adapters_list)):

    try:
        next_item = adapters_list[number + 1]
        if next_item - item == 1:
            start_chunk += 1
        elif next_item - item == 3:
            if start_chunk > 0:
                if start_chunk in cache.keys():
                    chunks.append(cache[start_chunk])
                else:
                    # Just in case there are bigger chunks, I can expand my cache.
                    print("You failed {}".format(start_chunk))
            start_chunk = -1
    except:
        print(chunks)
        print("Maybe {}".format(prod(chunks)))
