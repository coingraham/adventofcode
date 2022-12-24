from aocd.models import Puzzle
from operator import add
puzzle = Puzzle(year=2022, day=19)

# Merry Christmas everyone!!!
# Always test with the sample input first!!
sample_input = '''Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.'''

# create a robot bitwise map for the results dictionary
R = {x: 1 << i for i, x in enumerate(["o", "c", "b", "g"])}


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


def build(buy_robots, this_robot):

    if this_robot == "o":
        buy_robots[0] += 1
        return buy_robots
    if this_robot == "c":
        buy_robots[1] += 1
        return buy_robots
    if this_robot == "b":
        buy_robots[2] += 1
        return buy_robots
    if this_robot == "g":
        buy_robots[3] += 1
        return buy_robots


def pay(materials, blueprint):

    materials[0] -= blueprint[0]
    materials[1] -= blueprint[1]
    materials[2] -= blueprint[2]

    return materials


def alt_blueprint_geodes(blueprint, seen, minutes, materials, robots, results):
    best_geodes = materials[3]

    if seen not in results:
        results[seen] = best_geodes
        if best_geodes > results["best"]:
            results["best"] = best_geodes
    else:
        if best_geodes > results[seen]:
            results[seen] = max(results.get(seen, 0), best_geodes)
        else:
            if best_geodes + (robots[3] * minutes) + (minutes * (minutes - 1)) / 2 < results["best"]:
                return results

    if minutes == 0:
        return results

    # I'm going to take turns building each robot and embed a limit for each
    for decision in [("g", 12), ("b", 10), ("c", 10), ("o", 4)]:

        # Buy geode robot if possible
        if decision[0] == "g":
            # Check if you have obsidian robots
            if robots[2] == 0:
                continue

            # Check if you built beyond the max
            if decision[1] <= robots[3]:
                continue

            # Check if we already have the resources ore and obs or spend minutes
            needed = 0
            new_materials = materials.copy()
            new_robots = robots.copy()
            if new_materials[0] < blueprint[3][0] or new_materials[2] < blueprint[3][2]:
                while new_materials[0] < blueprint[3][0] or new_materials[2] < blueprint[3][2]:
                    new_materials = list(map(add, new_materials, new_robots))
                    needed += 1

                # Check if we're done
                if minutes - needed - 1 < 0:
                    continue

            new_robots = build(new_robots, decision[0])
            new_materials = pay(new_materials, blueprint[3])
            new_materials = list(map(add, new_materials, robots))
            alt_blueprint_geodes(blueprint,
                                 ",".join([str(i) for i in new_robots]),
                                 minutes - needed - 1,
                                 new_materials,
                                 new_robots,
                                 results)

        # Buy obsidian robot if possible
        if decision[0] == "b":
            # Check if you have clay robots
            if robots[1] == 0:
                continue

            # Check if you built beyond the max
            if decision[1] <= robots[2]:
                continue

            # Check if we already have the resources ore and obs or spend minutes
            needed = 0
            new_materials = materials.copy()
            new_robots = robots.copy()
            if new_materials[0] < blueprint[2][0] or new_materials[1] < blueprint[2][1]:
                while new_materials[0] < blueprint[2][0] or new_materials[1] < blueprint[2][1]:
                    new_materials = list(map(add, new_materials, new_robots))
                    needed += 1

                # Check if we're done
                if minutes - needed - 1 < 0:
                    continue

            new_robots = build(new_robots, decision[0])
            new_materials = pay(new_materials, blueprint[2])
            new_materials = list(map(add, new_materials, robots))
            alt_blueprint_geodes(blueprint,
                                 ",".join([str(i) for i in new_robots]),
                                 minutes - needed - 1,
                                 new_materials,
                                 new_robots,
                                 results)

        # Buy clay robot if possible
        if decision[0] == "c":
            # Check if you built beyond the max
            if decision[1] <= robots[1]:
                continue

            # Check if we already have the resources ore and obs or spend minutes
            needed = 0
            new_materials = materials.copy()
            new_robots = robots.copy()
            if new_materials[0] < blueprint[1][0]:
                while new_materials[0] < blueprint[1][0]:
                    new_materials = list(map(add, new_materials, new_robots))
                    needed += 1

                # Check if we're done
                if minutes - needed - 1 < 0:
                    continue

            new_robots = build(new_robots, decision[0])
            new_materials = pay(new_materials, blueprint[1])
            new_materials = list(map(add, new_materials, robots))
            alt_blueprint_geodes(blueprint,
                                 ",".join([str(i) for i in new_robots]),
                                 minutes - needed - 1,
                                 new_materials,
                                 new_robots,
                                 results)

        # Buy ore robot if possible
        if decision[0] == "o":
            # Check if you built beyond the max
            if decision[1] <= robots[0]:
                continue

            # Check if we already have the resources ore or spend minutes
            needed = 0
            new_materials = materials.copy()
            new_robots = robots.copy()
            if new_materials[0] < blueprint[0][0]:
                while new_materials[0] < blueprint[0][0]:
                    new_materials = list(map(add, new_materials, new_robots))
                    needed += 1

                # Check if we're done
                if minutes - needed - 1 < 0:
                    continue

            new_robots = build(new_robots, decision[0])
            new_materials = pay(new_materials, blueprint[0])
            new_materials = list(map(add, new_materials, robots))
            alt_blueprint_geodes(blueprint,
                                 ",".join([str(i) for i in new_robots]),
                                 minutes - needed - 1,
                                 new_materials,
                                 new_robots,
                                 results)

    # If no robot can be purchased we can wrap up
    for run in range(minutes):
        materials = list(map(add, materials, robots))

    results[seen] = max(results.get(seen, 0), materials[3])

    # print("Robots: {}\nMaterials: {}\nSeen: {}\n".format(robots, materials, seen))
    return results


def question1():
    # question_input = sample_input
    question_input = puzzle.input_data

    blueprints, blueprints_list = load_blueprints(question_input)

    minutes = 24

    quality_scores = 0
    for bpid, blueprint in enumerate(blueprints_list):
        if bpid >= 0:
            geode_results = alt_blueprint_geodes(blueprint, "1,0,0,0", minutes, [0, 0, 0, 0], [1, 0, 0, 0], {})
            # print("Geode: \n{}".format(geode_results))
            quality = max(geode_results.values())

            blueprint_id = bpid + 1
            print("Blueprint: {} - Quality Score: {}".format(blueprint_id, quality))
            quality_scores += blueprint_id * quality

    print("Final Quality Scores: {}".format(quality_scores))


def question2():
    # question_input = sample_input
    question_input = puzzle.input_data

    blueprints, blueprints_list = load_blueprints(question_input)

    minutes = 32

    quality_scores = 1
    for bpid, blueprint in enumerate(blueprints_list):
        if bpid <= 2:
            geode_results = alt_blueprint_geodes(blueprint, "1,0,0,0", minutes, [0, 0, 0, 0], [1, 0, 0, 0], {"best": 0})
            # print("Geode: \n{}".format(geode_results))
            quality = max(geode_results.values())

            blueprint_id = bpid + 1
            print("Blueprint: {} - Quality Score: {}".format(blueprint_id, quality))
            quality_scores *= quality

    print("Final Quality Scores: {}".format(quality_scores))


if __name__ == '__main__':
    # question1()
    question2()

