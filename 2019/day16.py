from collections import defaultdict
from itertools import cycle
from aocd.models import Puzzle
import time

puzzle = Puzzle(year=2019, day=16)


def get_pattern(digit):
    pattern = []
    base = [0, 1, 0, -1]
    for item in base:
        for i in range(digit):
            pattern.append(item)
    pattern.append(pattern.pop(0))
    return pattern


def FFT(input, digit):
    rotate = cycle(get_pattern(digit))
    total = sum([tup[0] * tup[1] for tup in zip(input, rotate) if tup[1] != 0])
    value = abs(total) % 10
    return value


# print(get_pattern(4))
# print(FFT([1,2,3,4,5,6,7,8], 2))
test = "12345678"
test2 = "80871224585914546619083218645595"
test3 = "03036732577212944063491565474664"


def process_FFT(input, start, size, section):
    step = 0
    while True:
        new_input = []
        for num, value in enumerate(input):
            new_input.append(FFT(input, num + 1))

        input = new_input
        step += 1

        if step == section:
            string_input = ''.join(str(x) for x in input)
            return string_input


def process_shortcut(input, last):
    rev_input = list(reversed(input))
    new = [rev_input.pop(0)]
    for item in rev_input:
        new.append((item + new[-1]) % 10)

    return list(reversed(new))


# Part One
# input = [int(x) for x in list(test2)]
# print(''.join(str(x) for x in process_FFT(input, 0))) # now this is broken....

# Part Two
my_time = time.time()
input_data = puzzle.input_data
print(input_data)
original_input = [int(x) for x in list(input_data)]
total_size = len(original_input) * 10000
start = int(''.join(str(x) for x in original_input[0:7]))
offset = total_size - start

input = [int(x) for x in list(input_data * 10000)]
output = input[-offset:]
last_one = input[-1]
for k in range(100):
    output = process_shortcut(output, last_one)

print(''.join(str(x) for x in output[:8]))
print(time.time() - my_time)
