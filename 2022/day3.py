from aocd.models import Puzzle
puzzle = Puzzle(year=2022, day=3)

# Merry Christmas everyone!!!
# Always test with the sample input first!!
sample_input = '''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw'''


def question1():
    # question_input = sample_input
    question_input = puzzle.input_data

    total_values = 0
    letter_value = ".abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for backpack in question_input.splitlines():
        n = len(backpack)
        first = backpack[:n//2]
        last = backpack[n//2:]

        for letter in first:
            if letter in last:
                total_values += letter_value.index(letter)
                break

    print(total_values)


def question2():
    # question_input = sample_input
    question_input = puzzle.input_data

    total_values = 0
    letter_value = ".abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    collect_backpacks = []
    for n, backpack in enumerate(question_input.splitlines()):

        collect_backpacks.append(backpack)

        if n % 3 == 2:
            for letter in collect_backpacks[0]:
                if letter in collect_backpacks[1] and letter in collect_backpacks[2]:
                    total_values += letter_value.index(letter)
                    collect_backpacks = []
                    break

    print(total_values)
    pass

    # print(results)


if __name__ == '__main__':
    question1()
    question2()

