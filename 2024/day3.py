from itertools import product

from aocd.models import Puzzle
puzzle = Puzzle(year=2024, day=3)

sample_data = '''xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))'''

# q_i = sample_data
q_i = puzzle.input_data

mul_pattern = r'mul\(\d{1,3},\d{1,3}\)'
do_pattern = r'do\(\)'
dont_pattern = r'don\'t\(\)'


import re
import math

def part_one():

    mul_total = 0
    for match in re.finditer(mul_pattern, q_i):
        mul_total += math.prod([*map(int, re.findall(r'\d+',match.group()))])

    return mul_total

def part_two():

    ordering = {}

    for match in re.finditer(mul_pattern, q_i):
        ordering[match.span()[0]] = math.prod([*map(int, re.findall(r'\d+',match.group()))])

    for match in re.finditer(do_pattern, q_i):
        ordering[match.span()[0]] = True

    for match in re.finditer(dont_pattern, q_i):
        ordering[match.span()[0]] = False

    mul_total = 0
    do = True
    for key, value in sorted(ordering.items()):
        if isinstance(value, bool):
            do = value
            continue

        if do:
            mul_total += value

    return mul_total








    return mul_total


if __name__ == '__main__':
    print(part_one())
    print(part_two())
