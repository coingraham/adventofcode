from aocd.models import Puzzle
puzzle = Puzzle(year=2024, day=2)

sample_data = '''7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9'''

# q_i = [[*map(int, n.split())] for n in sample_data.splitlines()]
q_i = [[*map(int, n.split())] for n in puzzle.input_data.splitlines()]

# print(q_i)


def check_report(report):
    dec = (-3, -2, -1)
    inc = (3, 2, 1)
    diffs = list(map(lambda x, y: x - y, report[1:], report[:-1]))
    return all(i in dec for i in diffs) or all(i in inc for i in diffs)


def part_one():

    valid = 0
    for report in q_i:
        if check_report(report):
            valid += 1

    return valid


def check_report_thorough(report):

    for i, item in enumerate(report):
        new_report = report.copy()
        new_report.pop(i)
        if check_report(new_report):
            return True

    return False


def part_two():
    valid, invalid = [], []

    for report in q_i:
        if check_report(report):
            valid.append(report)
        else:
            invalid.append(report)

    for report in invalid:
        if check_report_thorough(report):
            valid.append(report)

    return len(valid)


if __name__ == '__main__':
    print(part_one())
    print(part_two())
