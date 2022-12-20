from aocd.models import Puzzle
puzzle = Puzzle(year=2022, day=19)

# Merry Christmas everyone!!!
# Always test with the sample input first!!
sample_input = '''Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.'''


def load_blueprints(question_input):
    blueprints = {}
    blueprints_list = []

    for number, blueprint in enumerate(question_input.splitlines()):
        id = number + 1
        blueprint_split = blueprint.split(" ")
        ore_cost = (int(blueprint_split[6]), 0, 0)
        clay_cost = (int(blueprint_split[12]), 0, 0)
        obs_cost = (int(blueprint_split[18]), int(blueprint_split[21]), 0)
        geo_cost = (int(blueprint_split[27]), 0, int(blueprint_split[30]))
        blueprints[id] = {}
        # Ore will be abbreviated o
        blueprints[id]["o"] = ore_cost
        # Clay will be abbreviated c
        blueprints[id]["c"] = clay_cost
        # Obsidian will be abbreviated b
        blueprints[id]["b"] = obs_cost
        # Geodes will be abbreviated g
        blueprints[id]["g"] = geo_cost

        # I may need a list to cycle
        blueprints_list.append([ore_cost, clay_cost, obs_cost, geo_cost])

    return blueprints, blueprints_list


def get_blueprint_geodes(blueprint, seen, minutes, resources, geodes, results):
    # Record the results
    results[seen] = max(results.get(seen, 0), geodes)

    # Buy an ore robot

    # Buy a clay robot

    # Buy an obsidian robot
    # Check if I have clay robot (prereqs)

    # Buy a geode robot
    # Check if I have obsidian robot (prereqs)

    return results


def question1():
    question_input = sample_input
    # question_input = puzzle.input_data

    blueprints, blueprints_list = load_blueprints(question_input)

    minutes = 24

    geodes = []
    for blueprint in blueprints_list:
        geodes.append(get_blueprint_geodes(blueprint, "", minutes, [[1, 0, 0, 0], [1, 0, 0, 0]], 0, {}))



    print(blueprints)




    # print(results)


def question2():
    question_input = sample_input
    # question_input = puzzle.input_data

    # print(results)


if __name__ == '__main__':
    question1()
    # question2()

