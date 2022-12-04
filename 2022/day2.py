from aocd.models import Puzzle
puzzle = Puzzle(year=2022, day=2)

# Merry Christmas everyone!!!
# Always test with the sample input first!!
sample_input = '''A Y
B X
C Z'''


def question1():
    # question_input = sample_input
    question_input = puzzle.input_data
    win_list = {
        "A X": 4,  # Rock Rock Tie
        "A Y": 8,  # Rock Paper Win
        "A Z": 3,  # Rock Scissor Lose
        "B X": 1,  # Paper Rock Lose
        "B Y": 5,  # Paper Paper Tie
        "B Z": 9,  # Paper Scissor Win
        "C X": 7,  # Scissor Rock Win
        "C Y": 2,  # Scissor Paper Lose
        "C Z": 6,  # Scissor Scissor Tie
    }

    total_value = 0
    for result in question_input.splitlines():
        total_value += win_list[result]

    print(total_value)


def question2():
    # question_input = sample_input
    question_input = puzzle.input_data
    win_list = {
        "A X": 3,  # Rock Scissor Lose
        "A Y": 4,  # Rock Rock Tie
        "A Z": 8,  # Rock Paper Win
        "B X": 1,  # Paper Rock Lose
        "B Y": 5,  # Paper Paper Tie
        "B Z": 9,  # Paper Scissor Win
        "C X": 2,  # Scissor Paper Lose
        "C Y": 6,  # Scissor Scissor Tie
        "C Z": 7,  # Scissor Rock Win
    }

    total_value = 0
    for result in question_input.splitlines():
        total_value += win_list[result]

    print(total_value)


if __name__ == '__main__':
    # question1()
    question2()

