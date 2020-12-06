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
    # Found some sample code online that utilized translate and maketrans
    seatid_list.append(int(partition.translate(partition.maketrans("FLBR", "0011")), 2))

# Use the max function to get the max item of a list
print(max(seatid_list))

# Enumerate will walk through an iterator and return both the step and value.  This
# keeps you from having to save and track counters and counter += 1.
min_seatid = min(seatid_list)
for i, seat in enumerate(sorted(seatid_list)):
    # Variable i will start at zero and my data starts higher so I offset it looking
    # for the first time there is a gap
    if i + min_seatid != seat:
        # Once we find the gap the seat will be one higher so we subtract.  We could also
        # just return i + min_seatid instead.
        print(seat - 1)
        break
