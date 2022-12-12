from aocd.models import Puzzle
puzzle = Puzzle(year=2022, day=11)

# Merry Christmas everyone!!!
# Always test with the sample input first!!
sample_input = '''Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1'''


def load_monkeys(input):
    monkeys_split = input.split("\n\n")
    monkeys = {}

    for monkey_lines in monkeys_split:
        monkey = monkey_lines.splitlines()

        monkey_number = int(monkey[0].split(" ")[1].split(":")[0])
        monkeys[monkey_number] = {}

        starting_items = "".join(monkey[1].split(" ")[4:]).split(",")
        monkeys[monkey_number]["items"] = starting_items

        operation = "lambda old:{}".format(monkey[2].split("=")[-1])
        f = eval(operation)
        monkeys[monkey_number]["operation"] = f

        test = monkey[3].split(" ")[-1]
        monkeys[monkey_number]["test"] = int(test)

        if_true = monkey[4].split(" ")[-1]
        monkeys[monkey_number]["if_true"] = int(if_true)

        if_false = monkey[5].split(" ")[-1]
        monkeys[monkey_number]["if_false"] = int(if_false)

        monkeys[monkey_number]["activity"] = 0

    return monkeys, len(monkeys_split)


def load_monkeys2(input):
    monkeys_split = input.split("\n\n")
    monkeys = {}
    primes = 1

    for monkey_lines in monkeys_split:
        monkey = monkey_lines.splitlines()

        monkey_number = int(monkey[0].split(" ")[1].split(":")[0])
        monkeys[monkey_number] = {}

        starting_items = "".join(monkey[1].split(" ")[4:]).split(",")
        monkeys[monkey_number]["items"] = starting_items

        operation = "lambda old:{}".format(monkey[2].split("=")[-1])
        f = eval(operation)
        monkeys[monkey_number]["operation"] = f

        prime = int(monkey[3].split(" ")[-1])
        primes *= prime

        test = monkey[3].split(" ")[-1]
        monkeys[monkey_number]["test"] = int(test)

        if_true = monkey[4].split(" ")[-1]
        monkeys[monkey_number]["if_true"] = int(if_true)

        if_false = monkey[5].split(" ")[-1]
        monkeys[monkey_number]["if_false"] = int(if_false)

        monkeys[monkey_number]["activity"] = 0

    return monkeys, len(monkeys_split), primes


def get_monkey_business(monkeys):
    monkey_business = []
    for monkey in monkeys.keys():
        monkey_business.append(monkeys[monkey]["activity"])
        print("Monkey {} inspected items {} times.".format(monkey, monkeys[monkey]["activity"]))

    return monkey_business


def question1():
    question_input = sample_input
    # question_input = puzzle.input_data

    rounds = 20
    monkeys, number_of_monkeys = load_monkeys(question_input)

    for round in range(rounds):
        for monkey_number in range(number_of_monkeys):
            for each in range(len(monkeys[monkey_number]["items"])):
                # Pop the item out of the list
                item = int(monkeys[monkey_number]["items"].pop(0))

                # Monkey inspects the item
                item = monkeys[monkey_number]["operation"](item)

                # Monkey gets bored
                item = item // 3

                # Monkey tests the item
                if item % monkeys[monkey_number]["test"] == 0:
                    receiver = monkeys[monkey_number]["if_true"]

                    # Throw if true
                    monkeys[receiver]["items"].append(item)

                else:
                    receiver = monkeys[monkey_number]["if_false"]

                    # Throw if false
                    monkeys[receiver]["items"].append(item)

                # Update monkey activity
                monkeys[monkey_number]["activity"] += 1

    monkey_business = []
    for monkey in monkeys.keys():
        monkey_business.append(monkeys[monkey]["activity"])

    monkey_business.sort()

    print(monkey_business[-2] * monkey_business[-1])


def question2():
    # question_input = sample_input
    question_input = puzzle.input_data

    rounds = 10000
    monkeys, number_of_monkeys, primes = load_monkeys2(question_input)
    interesting = [9999]

    for round in range(rounds):
        for monkey_number in range(number_of_monkeys):
            for each in range(len(monkeys[monkey_number]["items"])):
                # Pop the item out of the list
                item = int(monkeys[monkey_number]["items"].pop(0))

                # Monkey inspects the item
                item = monkeys[monkey_number]["operation"](item)

                # Manage the item size
                # Modulo arithmetic FTW
                item = item % primes

                # Monkey tests the item
                if item % monkeys[monkey_number]["test"] == 0:
                    receiver = monkeys[monkey_number]["if_true"]

                    # Throw if true
                    monkeys[receiver]["items"].append(item)

                else:
                    receiver = monkeys[monkey_number]["if_false"]

                    # Throw if false
                    monkeys[receiver]["items"].append(item)

                # Update monkey activity
                monkeys[monkey_number]["activity"] += 1

        if round in interesting:
            print("== After round {} ==".format(round + 1))
            monkey_business = get_monkey_business(monkeys)

            monkey_business.sort()
            print(monkey_business[-2] * monkey_business[-1])


if __name__ == '__main__':
    question1()
    question2()

