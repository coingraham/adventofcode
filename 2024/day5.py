from aocd.models import Puzzle
puzzle = Puzzle(year=2024, day=5)

sample_data = '''47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47'''

# q_i = [n for n in sample_data.splitlines()]
q_i = [n for n in puzzle.input_data.splitlines()]

# Process inputs
import collections as col

followers = col.defaultdict(list)
leaders = col.defaultdict(list)
updates = []
non_compliant = []
for line in q_i:
    # Get all the rules
    if "|" in line:
        i, j = map(int, line.split('|'))

        # I like making dictionaries both ways
        followers[i].append(j)
        leaders[j].append(i)

    # Get all the updates
    if "," in line:
        updates.append([*map(int, line.split(","))])


def check_values(update):
    for i, item in enumerate(update):
        # skip the first, it doesn't matter
        if i == 0:
            continue

        # if you made it to the end your good
        if i == len(update) - 1:
            middle = i // 2
            return update[middle]

        # check middle, are its numbers before and after correct?
        for follower in followers.get(item, []):
            if follower in update and update.index(follower) < i:
                return False

        for leader in leaders.get(item, []):
            if leader in update and update.index(leader) > i:
                return False


def part_one():
    good_updates = []
    for update in updates:
        if middle := check_values(update):
            good_updates.append(middle)
        else:
            non_compliant.append(update)

    return sum(good_updates)


def check_values_with_fix(update):
    for i, item in enumerate(update):
        if i == 0:
            continue

        if i == len(update) - 1:
            middle = i // 2
            return update[middle]

        # check middle, are its numbers before and after correct?
        for follower in followers.get(item, []):
            if follower in update and update.index(follower) < i:
                update.insert(i, update.pop(update.index(follower)))
                return update

        for leader in leaders.get(item, []):
            if leader in update and update.index(leader) > i:
                update.insert(i, update.pop(update.index(leader)))
                return update

def part_two():
    fixed_updates = []
    for update in non_compliant:
        while True:
            result = check_values_with_fix(update)

            if isinstance(result, int):
                fixed_updates.append(result)
                break

            update = result

    return sum(fixed_updates)


if __name__ == '__main__':
    print(part_one())
    print(part_two())
