from aocd.models import Puzzle
puzzle = Puzzle(year=2022, day=4)

# Merry Christmas everyone!!!
# Always test with the sample input first!!
sample_input = '''2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8'''


def question1():
    # question_input = sample_input
    question_input = puzzle.input_data

    duplicates = 0

    for id_numbers in question_input.splitlines():
        first, second = id_numbers.split(",")
        first_start, first_stop = first.split("-")
        second_start, second_stop = second.split("-")

        first_set = {i for i in range(int(first_start), int(first_stop) + 1)}
        second_set = {i for i in range(int(second_start), int(second_stop) + 1)}
        union_len = len(first_set | second_set)

        if union_len == len(first_set) or union_len == len(second_set):
            duplicates += 1

    print(duplicates)


def question2():
    # question_input = sample_input
    question_input = puzzle.input_data

    duplicates = 0

    for id_numbers in question_input.splitlines():
        first, second = id_numbers.split(",")
        first_start, first_stop = first.split("-")
        second_start, second_stop = second.split("-")

        first_set = {i for i in range(int(first_start), int(first_stop) + 1)}
        second_set = {i for i in range(int(second_start), int(second_stop) + 1)}
        union_len = len(first_set | second_set)

        if union_len != len(first_set) + len(second_set):
            duplicates += 1

    print(duplicates)


if __name__ == '__main__':
    question1()
    question2()

