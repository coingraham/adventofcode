from aocd.models import Puzzle
puzzle = Puzzle(year=2021, day=6)

sample_data = '''3,4,3,1,2'''

# question_input = [int(n) for n in sample_data.split(",")]
question_input = [int(n) for n in puzzle.input_data.split(",")]


def part_one(initial, day_limit):
    next_day = []
    add_fish = 0
    days = 0
    while True:
        if days == day_limit:
            break

        for fish in initial:
            if fish == 0:
                next_day.append(6)
                add_fish += 1
            else:
                next_day.append(fish - 1)
        
        days += 1
        for n in range(add_fish):
            next_day.append(8)
        initial = next_day
        next_day = []
        add_fish = 0

        if days % 7 == 0:
            initial.sort()
            print(initial)

    return len(initial)
        


def part_two(initial, days_limit):
    fish_lives = {
        0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0,
    }
    for fish in initial:
        fish_lives[fish] += 1
    days = 0
    hold = 0
    while True:
        if days == days_limit:
            break

        hold = fish_lives[0]
        for item in range(8):
            fish_lives[item] = fish_lives[item + 1]
        
        fish_lives[6] += hold
        fish_lives[8] = hold
        
        days += 1

    return sum(fish_lives.values())


if __name__ == '__main__':
    # print(part_one(question_input, 80))
    print(part_two(question_input, 256))
