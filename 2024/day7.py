from aocd.models import Puzzle
puzzle = Puzzle(year=2024, day=7)

sample_data = '''190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20'''

# q_i = [(int(i.strip()), list(map(int, j.split()))) for i, j in (n.split(":") for n in sample_data.splitlines())]
q_i = [(int(i.strip()), list(map(int, j.split()))) for i, j in (n.split(":") for n in puzzle.input_data.splitlines())]


def find_operands(digits, answer, target, updated=False):
    # Base condition
    if not digits:
        return answer == target

    # Get the next digit
    next_digit = digits.pop(0)

    # Try adding this next digit
    if find_operands(digits, answer + next_digit, target):
        return True

    # Try multiplying this next digit
    if find_operands(digits, answer * next_digit, target):
        return True

    # Nothing worked, put it back
    digits.insert(0, next_digit)
    return False


def find_operands_v2(digits, answer, target):
    # Base condition
    if not digits:
        return answer == target

    # Get the next digit
    next_digit = digits.pop(0)

    # Try adding this next digit
    if find_operands_v2(digits, answer + next_digit, target):
        return True

    # Try multiplying this next digit
    if find_operands_v2(digits, answer * next_digit, target):
        return True

    # Try concatenating this next digit
    if find_operands_v2(digits, int(str(answer) + str(next_digit)), target):
        return True

    # Nothing worked, put it back
    digits.insert(0, next_digit)
    return False

def part_one(calibrations):
    sum_of_test_values = 0
    for calibration in calibrations:
        if find_operands(calibration[1], calibration[1].pop(0), calibration[0]):
            sum_of_test_values += calibration[0]

    return sum_of_test_values


def part_two(calibrations):
    sum_of_test_values = 0
    for calibration in calibrations:
        if find_operands_v2(calibration[1], calibration[1].pop(0), calibration[0]):
            sum_of_test_values += calibration[0]

    return sum_of_test_values


if __name__ == '__main__':
    import copy
    print(part_one(copy.deepcopy(q_i)))
    print(part_two(copy.deepcopy(q_i)))
