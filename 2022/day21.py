from aocd.models import Puzzle
puzzle = Puzzle(year=2022, day=21)

# Merry Christmas everyone!!!
# Always test with the sample input first!!
sample_input = '''root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32'''


def load_monkeys(question_input):

    monkey_list = []
    monkey_values = {}

    for monkey in question_input.splitlines():
        source, yell = monkey.split(": ")

        if yell.isdigit():
            monkey_values[source] = int(yell)

        else:
            yellings = yell.split(" ")
            monkey_list.append([source, yellings[0], yellings[1], yellings[2]])

    return monkey_list, monkey_values


def load_monkeys_not_human(question_input):

    monkey_values = {}

    for monkey in question_input.splitlines():
        source, yell = monkey.split(": ")

        if source == "humn":
            continue

        if yell.isdigit():
            monkey_values[source] = int(yell)

        else:
            monkey_values[source] = yell

    return monkey_values


def question1():
    # question_input = sample_input
    question_input = puzzle.input_data

    monkey_list, monkey_values = load_monkeys(question_input)

    while monkey_list:
        # Get the front of the list
        this_monkey = monkey_list.pop(0)
        name, first, op, second = this_monkey

        # Check if values are available
        if first in monkey_values and second in monkey_values:
            # Do the operation and save
            if op == "+":
                monkey_values[name] = monkey_values[first] + monkey_values[second]
            if op == "-":
                monkey_values[name] = monkey_values[first] - monkey_values[second]
            if op == "*":
                monkey_values[name] = monkey_values[first] * monkey_values[second]
            if op == "/":
                monkey_values[name] = int(monkey_values[first] / monkey_values[second])
        else:
            # Can't do it so put it back on the stack
            monkey_list.append(this_monkey)

    print(monkey_values["root"])


def question2():
    # question_input = sample_input
    question_input = puzzle.input_data

    # I can use mathematics to balance the equation and solve for humn instead of guessing
    monkey_list, monkey_values = load_monkeys(question_input)
    del monkey_values["humn"]

    for count in range(100_000):

        # Get the front of the list
        this_monkey = monkey_list.pop(0)
        name, first, op, second = this_monkey

        # Check if values are available
        if first in monkey_values and second in monkey_values:
            # Do the operation and save
            if op == "+":
                monkey_values[name] = monkey_values[first] + monkey_values[second]
            if op == "-":
                monkey_values[name] = monkey_values[first] - monkey_values[second]
            if op == "*":
                monkey_values[name] = monkey_values[first] * monkey_values[second]
            if op == "/":
                monkey_values[name] = int(monkey_values[first] / monkey_values[second])

            del monkey_values[first]
            del monkey_values[second]
        else:
            monkey_list.append([name, first, op, second])

    monkey_dictionary = {}
    for monkey in monkey_list:
        name, first, op, second = monkey

        monkey_dictionary[name] = [first, op, second]

    # Starting to solve for the humn by mathematics.  Imagining as left and right sides of an equation
    for option in monkey_dictionary["root"]:
        if option in monkey_values:
            value = monkey_values[option]

        if option in monkey_dictionary.keys():
            follow = option
    del monkey_dictionary["root"]

    # I need to cycle through the root operation and replace the parts
    while follow != "humn":
        new_left, op, new_right = monkey_dictionary[follow]

        # division
        if op == "/":
            if new_left in monkey_values:
                follow = new_right
                value = monkey_values[new_left] / value

            else:
                follow = new_left
                value = value * monkey_values[new_right]

        # multiplication
        if op == "*":
            if new_left in monkey_values:
                follow = new_right
                value = int(value / monkey_values[new_left])

            else:
                follow = new_left
                value = int(value / monkey_values[new_right])

        # subtraction
        if op == "-":
            if new_left in monkey_values:
                follow = new_right
                value = monkey_values[new_left] - value

            else:
                follow = new_left
                value = value + monkey_values[new_right]

        # addition
        if op == "+":
            if new_left in monkey_values:
                follow = new_right
                value = value - monkey_values[new_left]

            else:
                follow = new_left
                value = value - monkey_values[new_right]

    print(value)


if __name__ == '__main__':
    question1()
    question2()

