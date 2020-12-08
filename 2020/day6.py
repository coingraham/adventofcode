from aocd.models import Puzzle
puzzle = Puzzle(year=2020, day=6)

example = """abc

a
b
c

ab
ac

a
a
a
a

b"""

# groups = example.split("\n")
groups = puzzle.input_data.split("\n")


# Collect groups into sets of customs declarations - part one
def collect_groups_anyone(groups):
    declarations = []
    temp_declarations = set([])
    for group in groups:
        if group == '':
            declarations.append(temp_declarations.copy())
            temp_declarations.clear()
        else:
            for question in list(group):
                temp_declarations.add(question)

    # We do one final append in case the last line isn't ''
    declarations.append(temp_declarations)
    return declarations


# Collect groups into sets of customs declarations - part two
def collect_groups_everyone(groups):
    declarations = []
    temp_declarations = [0, set([])]
    for group in groups:
        if group == '':
            declarations.append(temp_declarations[1])
            temp_declarations = [0, set([])]
        else:
            if temp_declarations[0]:
                individual = set([])
                for question in list(group):
                    individual.add(question)
                temp_declarations[1] = temp_declarations[1].intersection(individual)
                individual.clear()
            else:
                for question in list(group):
                    temp_declarations[1].add(question)
                    temp_declarations[0] += 1

    # We do one final append in case the last line isn't ''
    declarations.append(temp_declarations[1])
    return declarations


# Sum the declarations
def sum_declarations(declarations):
    total = 0
    for declaration in declarations:
        total += len(declaration)
    return total


if __name__ == '__main__':
    print(sum_declarations(collect_groups_anyone(groups)))
    print(sum_declarations(collect_groups_everyone(groups)))
