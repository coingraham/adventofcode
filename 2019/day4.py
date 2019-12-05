import aoc_common as ac
from aocd.models import Puzzle

puzzle = Puzzle(year=2019, day=4)

print(puzzle.input_data)

counter_a = 0
counter_b = 0
for num in range(168630, 718099):
    number_list = [int(x) for x in str(num)]
    if ac.every_digit_greater_equal(number_list):
        if len(number_list) != len(set(number_list)):
            counter_a += 1
            for item in number_list:
                if number_list.count(item) == 2:
                    counter_b += 1
                    break


print(counter_a)
print(puzzle.answer_a)
# puzzle.answer_a = counter_a

print(counter_b)
print(puzzle.answer_b)
# puzzle.answer_b = counter_b


# Found on reddit was very interesting
print(sum(1 for s in map(str, range(168630, 718099))
          if list(s) == sorted(s) and 2 in [s.count(i) for i in s]))
