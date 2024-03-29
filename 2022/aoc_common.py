

# Step up, down, left, right - complex point
def get_steps(my_map, memo, point):
    paths = []
    height = len(my_map) - 1
    width = len(my_map[0]) - 1

    # Get up step
    up = point + 1j

    # Check if this step is outside the map
    if 0 <= int(up.real) <= width and 0 <= int(up.imag) <= height:
        up_point = "{}_{}".format(int(up.real), int(up.imag))

        # Check if we've stepped here before
        if up_point not in memo:
            paths.append(up)

    # Get down step
    down = point - 1j

    # Check if this step is outside the map
    if 0 <= int(down.real) <= width and 0 <= int(down.imag) <= height:
        down_point = "{}_{}".format(int(down.real), int(down.imag))

        # Check if we've stepped here before
        if down_point not in memo:
            paths.append(down)

    # Get right step
    right = point + 1

    # Check if this step is outside the map
    if 0 <= int(right.real) <= width and 0 <= int(right.imag) <= height:
        right_point = "{}_{}".format(int(right.real), int(right.imag))

        # Check if we've stepped here before
        if right_point not in memo:
            paths.append(right)

    # Get left step
    left = point - 1

    # Check if this step is outside the map
    if 0 <= int(left.real) <= width and 0 <= int(left.imag) <= height:
        left_point = "{}_{}".format(int(left.real), int(left.imag))

        # Check if we've stepped here before
        if left_point not in memo:
            paths.append(left)

    # Return the path options
    return paths

# ****As seen in someone else's code*****
# Starting with a list of unique items, I want to be able to use set theory to quickly know
# are they the same, different, included, excluded
my_list = {
    "frank": 0,
    "mary": 0,
    "jerome": 0,
    "maria": 0
}

# for each item build a bitwise representation
bitwise_map = {x: 1 << i for i, x in enumerate(my_list)}

print(bitwise_map)

# Create a collection with frank and maria
collection1 = bitwise_map["frank"] | bitwise_map["maria"]

# Is jerome in the collection?
print(bool(bitwise_map["jerome"] & collection1))

# Is maria in the collection?
print(bool(bitwise_map["maria"] & collection1))


