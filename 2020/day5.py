from aocd.models import Puzzle
puzzle = Puzzle(year=2020, day=5)

example = """BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL"""

partitions = puzzle.input_data.split("\n")
# partitions = example.split("\n")

# Starting out, they mention (and highlighted) the word 'binary' which should
# kick off coding spidey sense.  Hopefully you did some tests and discovered
# that if you treated the code BFFFBBF as a binary number 1000110 it
# equals 70 (64 + 6 + 4)

# In python you can convert a string to a number using int(str) but you can also
# give a second argument to use that base for conversion.  So int("1000110", 2) = 70

# Here we collect all the seat ids so we can find a max, we also need this for part 2.
seatid_list = []
for partition in partitions:
    # You can reference a string like a list to do string slicing.  And you can use
    # negative numbers to walk back from the end.  "TESTING"[-3:] would give "ING"
    row = partition[:-3].replace("F", "0").replace("B", "1")
    column = partition[-3:].replace("L", "0").replace("R", "1")
    seatid_list.append((int(row, 2) * 8) + int(column, 2))

# Use the max function to get the max item of a list
print(max(seatid_list))

# Enumerate will walk through an iterator and return both the step and value.  This
# keeps you from having to save and track counters and counter += 1.
for i, seat in enumerate(sorted(seatid_list)):
    # Variable i will start at zero and my data starts at 51 so I offset it looking
    # for the first time there is a gap
    if i + 51 != seat:
        # Once we find the gap the seat will be one higher so we subtract.  We could also
        # just return i + 51 instead.
        print(seat - 1)
        break
