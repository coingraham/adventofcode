from aocd.models import Puzzle
puzzle = Puzzle(year=2020, day=7)

example = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""

example2 = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""

example3 = """shiny gold bags contain 2 dark red bags.
dark red bags contain 3 dark orange bags, 4 dark blue bags.
dark orange bags contain no other bags.
dark blue bags contain no other bags."""

# rules = example.split("\n")
# rules = example2.split("\n")
rules = example3.split("\n")
# rules = puzzle.input_data.split("\n")

# Gather colors and relationships.  Maybe work backwards from inside out.
backward_relationships = {}
forward_relationships = {}

for rule in rules:
    start, end = rule.split(" contain ")
    start_color = " ".join(start.split(" ")[:-1])
    end_parts = end.split(", ")
    for item in end_parts:
        number = item.split(" ")[0]
        end_color = " ".join(item.split(" ")[1:-1])

        if start_color not in forward_relationships:
            forward_relationships[start_color] = []
        forward_relationships[start_color].append((end_color, number))

        if end_color not in backward_relationships:
            backward_relationships[end_color] = []
        backward_relationships[end_color].append((start_color, number))


# Walk the relationships (backward) and discover the sources. Recursive.
def walk_relationship(relationships, starting_point, path_list):
    if starting_point in relationships.keys():
        for path in relationships[starting_point]:
            if path[0] not in path_list:
                path_list.append(path[0])
                walk_relationship(relationships, path[0], path_list)

    return len(path_list)


def walk_relationship_alt(relationships, starting_point_bag):
    bag_list = []
    if starting_point_bag in relationships.keys():
        for child_bag in relationships[starting_point_bag]:
            color = child_bag[0]
            if color not in bag_list:
                bag_list.append(color)
                bag_list.extend(walk_relationship_alt(relationships, color))

    return bag_list


def walk_relationship_with_counts(relationships, starting_point, previous, answer_list):
    if starting_point in relationships.keys():
        for path in relationships[starting_point]:
            if path[0] == "other":
                return

            else:
                current = previous * int(path[1])
                answer_list.append(current)
                walk_relationship_with_counts(relationships, path[0], current, answer_list)

    return sum(answer_list)


def walk_relationship_with_counts_alt(relationships, starting_color, previous_bag_count):
    answer = 0
    for child_bag in relationships[starting_color]:
        color = child_bag[0]
        if color == "other":
            return 0
        else:
            current_bag_count = int(child_bag[1])
            multiplier = previous_bag_count * current_bag_count
            answer += multiplier + walk_relationship_with_counts_alt(relationships, color, multiplier)

    return answer


# print(walk_relationship(backward_relationships, "shiny gold", []))
print(walk_relationship_with_counts(forward_relationships, "shiny gold", 1, []))

# print(len(set(walk_relationship_alt(backward_relationships, "shiny gold"))))
print(walk_relationship_with_counts_alt(forward_relationships, "shiny gold", 1))
