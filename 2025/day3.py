from aocd.models import Puzzle

puzzle = Puzzle(year=2025, day=3)

sample_data = """559555555444844433333222111
987654321111111
811111111111119
234234234234278
818181911112111"""

# question input
# q_i = [n for n in sample_data.splitlines()]
q_i = [n for n in puzzle.input_data.splitlines()]

def part_one():
    max_numbers = []
    for bank in q_i:
        digits = [int(d) for d in bank]
        max_first = max(digits[:-1])
        max_first_position = digits.index(max_first)
        max_second = max(digits[max_first_position + 1:])
        # max_second_position = digits.index(max_second)

        max_numbers.append(int("".join([str(max_first), str(max_second)])))

    return sum(max_numbers)

def part_two():
    max_numbers = []
    for bank in q_i:
        digits = [int(d) for d in bank]
        beginning = digits[:-12]
        ending = digits[-12:]

        # Phase one, find all the maxes up to the last 12 digits
        max_beginning = []

        while beginning:
            max_first = max(beginning)
            max_first_position = beginning.index(max_first)
            max_beginning.append(max_first)
            beginning = beginning[max_first_position + 1:]

        # Phase two, combine with the end and sort out the maxes by comparison
        new_digits = max_beginning + ending
        initial_runs = True
        while len(new_digits) > 12:
            if initial_runs:
                new_digits, initial_runs = check_forward(new_digits, initial_runs)
            else:
                new_digits = check_backward(new_digits)

        max_numbers.append(int("".join(map(str, new_digits))))

    return sum(max_numbers)


def check_forward(new_digits, initial_runs):
    for i, digit in enumerate(new_digits):
        if i == 0:
            continue
        if initial_runs:
            if digit > new_digits[i - 1]:
                new_digits.pop(i - 1)
                return new_digits, True

    return new_digits, False

def check_backward(new_digits):
    digits_lenth = len(new_digits)
    for i in range(digits_lenth - 1, -1, -1):
        if i == digits_lenth - 1:
            continue

        if new_digits[i] >= new_digits[i + 1]:
            new_digits.pop(i + 1)
            return new_digits

if __name__ == '__main__':
    # print(part_one())
    print(part_two())
