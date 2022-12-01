from aocd.models import Puzzle
puzzle = Puzzle(year=2022, day=1)

# Merry Christmas everyone!!!
# Always test with the sample input first!!
sample_input = '''1000
2000
3000

4000

5000
6000

7000
8000
9000

10000'''


def question1():
    # I tested my code with this first.
    question_input = sample_input

    # This is the real question input.
    # question_input = puzzle.input_data

    # I'll use this variable to track the largest calorie total.
    largest_calories = 0

    # I'll use this to add up the snacks' calories for a temporary total.
    elf_calorie_sum = 0

    # I'll loop through the question input one line at a time adding the calories
    # as I go.  When I hit a blank line, i'll compare to the largest, and reset the
    # counter to 0 for the next elf.
    for line in question_input.splitlines():

        # This is a shorthand way of writing "if the line is not defined", this
        # will get triggered on the blank lines in between elves.
        if not line:

            # Compare the elf's current total to the largest.  If it's bigger
            # then update the variable.
            if elf_calorie_sum > largest_calories:
                largest_calories = elf_calorie_sum

            # If it's smaller, just reset the temporary calories and move on to the
            # next elf.
            elf_calorie_sum = 0

        else:
            # The line has a value, add it to the elf's temporary total
            elf_calorie_sum += int(line)

    print(largest_calories)


def question2():
    # I tested my code with this first.
    question_input = sample_input

    # This is the real question input.
    # question_input = puzzle.input_data

    # I've decided to not throw away any calorie totals but keep them in a list.
    calorie_list = []

    # Same as before.
    elf_calorie_sum = 0

    # Why do I need this here?  If you comment it out, you get the wrong
    # answer.  Can you figure out the bug?
    question_input += "\n\n"

    # Same as before
    for line in question_input.splitlines():

        # Same as it ever was
        if not line:

            # Here I do no comparison, but just append all the calorie totals
            # to the end of the list.
            calorie_list.append(elf_calorie_sum)

            # Reset for the next elf.
            elf_calorie_sum = 0

        else:
            # Same as before
            elf_calorie_sum += int(line)

    # Now I have a list of calorie totals but in any order.  So I sort the list
    # from greatest to least.
    calorie_list.sort(reverse=True)

    # Then I slice the first three elements from the list and pass them to sum.
    print(sum(calorie_list[0:3]))


if __name__ == '__main__':
    question1()
    question2()

