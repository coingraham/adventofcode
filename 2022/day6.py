from aocd.models import Puzzle
puzzle = Puzzle(year=2022, day=6)

# Merry Christmas everyone!!!
# Always test with the sample input first!!
sample_input = '''mjqjpqmgbljsphdztnvjfqwrcgsmlb
bvwbjplbgvbhsrlpgdmjqwftvncz
nppdvjthqldpwncqszvftbrmjlhg
nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg
zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'''


def question1():
    # question_input = sample_input
    question_input = puzzle.input_data

    starting_point = 4

    marker = 0
    for line in question_input.splitlines():
        for i in range(len(line)):
            grouping = line[i:i + starting_point]
            unique_grouping = set(grouping)
            if len(grouping) == len(unique_grouping):
                marker = i + starting_point
                print(marker)
                break


def question2():
    # question_input = sample_input
    question_input = puzzle.input_data

    starting_point = 14

    marker = 0
    for line in question_input.splitlines():
        for i in range(len(line)):
            grouping = line[i:i + starting_point]
            unique_grouping = set(grouping)
            if len(grouping) == len(unique_grouping):
                marker = i + starting_point
                print(marker)
                break


if __name__ == '__main__':
    question1()
    question2()

