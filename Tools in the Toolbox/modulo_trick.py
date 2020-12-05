## The modulo trick

# Often in AOC puzzles you'll find that you need to cycle through a list of numbers
# and then come back to the front and start over cycling through the list again.  There's
# couple of ways to accomplish this.

# First you can check if the index is higher than the max list length and subtract like this:
print("Cycle using subtraction:")
my_list = [1, 2, 3]
length = len(my_list)
index_number = 0

# loop over the list 6 iterations, this would normally fail at mylist[3]
for x in range(6):
    if index_number >= length:
        index_number -= length

    print(my_list[index_number])
    index_number += 1

# But this is complicated and not very elegant.  Luckily we have another option using
# modulo.  Modulo is the remainder in division, and the remainder happens to cycle in
# same way that we want.  For example:

# 0 / 3 = 0 R 0
# 1 / 3 = 0 R 1
# 2 / 3 = 0 R 2
# 3 / 3 = 1 R 0
# 4 / 3 = 1 R 1
# 5 / 3 = 1 R 2
# 6 / 3 = 2 R 0

# Notice how the remainder cycles 0, 1, 2, 0, 1, 2, 0, 1, 2 while the divisor counts up.  Modulo
# in python is written with the percent sign so the above looks like this:

# 0 % 3 = 0
# 1 % 3 = 1
# 2 % 3 = 2
# 3 % 3 = 0
# 4 % 3 = 1
# 5 % 3 = 2
# 6 % 3 = 0

# So with this our code becomes:
print("\nCycle using modulo:")
my_list = [1, 2, 3]
length = len(my_list)

# loop over the list 6 iterations, this would normally fail at mylist[3]
for x in range(6):
    index_number = x % length
    print(my_list[index_number])  # "%" is the symbol for modulo in python


# Now you know!