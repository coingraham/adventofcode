from aocd.models import Puzzle
puzzle = Puzzle(year=2022, day=9)

# Merry Christmas everyone!!!
# Always test with the sample input first!!
sample_input = '''R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2'''

sample_input2 = '''R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20'''


# Pulled code from AOC 2019
def get_complex_distance(complex1, complex2):
    x_diff = int(abs(complex1.real - complex2.real))
    y_diff = int(abs(complex1.imag - complex2.imag))
    return max(x_diff, y_diff)


# New for question 2.  I "cheated" on the first one and didn't
# calculate the move live.  I just remembered the last spot and
# moved there.  Now I need to figure it out.
def get_complex_distance_and_move(complex1, complex2):
    x_diff = int(complex1.real - complex2.real)
    y_diff = int(complex1.imag - complex2.imag)
    max_diff = max(abs(x_diff), abs(y_diff))
    if x_diff == -2 or x_diff == 2:
        x_diff = x_diff // 2
    if y_diff == -2 or y_diff == 2:
        y_diff = y_diff // 2

    return max_diff, complex(x_diff, y_diff)


def question1():
    # question_input = sample_input
    question_input = puzzle.input_data

    s = complex(0, 0)
    H = complex(0, 0)
    previous_H = complex(0, 0)
    T = complex(0, 0)
    tracker = {
        complex(0, 0): None
    }

    directional_map = {
        "U": complex(0, 1),
        "D": complex(0, -1),
        "L": complex(-1, 0),
        "R": complex(1, 0)
    }

    # Loop over the movement command
    for movement in question_input.splitlines():
        direction, number = movement.split(" ")

        # Move the Head knot
        for move in range(int(number)):
            previous_H = H
            H += directional_map[direction]

            # Evaluate the Tail knot
            H_T_distance = get_complex_distance(H, T)
            if H_T_distance > 1:
                T = previous_H

                # Record the Tail position
                tracker[T] = None

    print(len(tracker.keys()))


def question2():
    # question_input = sample_input2
    question_input = puzzle.input_data

    # Build a list of 10 knots H plus 1 - 9.
    knots = [complex(0, 0) for i in range(10)]

    # We track the progress of the last knot for the answer
    tracker_of_9 = {
        complex(0, 0): None
    }

    # Makes it super easy to move the first knot
    directional_map = {
        "U": complex(0, 1),
        "D": complex(0, -1),
        "L": complex(-1, 0),
        "R": complex(1, 0)
    }

    # Loop over the movement command
    for movement in question_input.splitlines():
        direction, number = movement.split(" ")

        # Move the Head knot
        for move in range(int(number)):
            knots[0] += directional_map[direction]

            # Evaluate all the other knots one at a time
            for position in range(1, len(knots)):

                # I've updated the function to get the distance and send the adjustment back
                knot_distance, adjustment = get_complex_distance_and_move(knots[position - 1], knots[position])
                if knot_distance > 1:
                    knots[position] += adjustment
                else:
                    # If one knot doesn't move, the rest after will not move either.
                    break

            # Record the Tail position
            tracker_of_9[knots[9]] = None

    print(len(tracker_of_9.keys()))


if __name__ == '__main__':
    question1()
    question2()

