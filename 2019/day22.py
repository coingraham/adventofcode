from collections import deque
import aoc_common as ac
import day22_input as d22

# deck_size = 10007
deck_size = 10
# deck_size = 119315717514047
# deck_size = 10
deck = deque([x for x in range(deck_size)])

test = """deal into new stack
cut -2
deal with increment 7
cut 8
cut -4
deal with increment 7
cut 3
deal with increment 9
deal with increment 3
cut -1
"""

test2 = """deal with increment 7
deal with increment 9
cut -2"""

# lines = test2.splitlines()
lines = d22.shorter.splitlines()
# lines = d22.input.splitlines()
# lines = test2.splitlines()


def deal(d):
    d.reverse()
    return d


def deal_card(position, size):
    return size - position


def deal_card_rev(position, size):
    return size - position - 1


def cut(n, d):
    d.rotate(-n)
    return d


def test_cut_rev(n, d):
    d.rotate(n)
    return d


def cut_card(position, n, size):
    if position >= n:
        return position - n
    else:
        return size - n + position


def cut_card_rev(position, n, size):
    if position <= n:
        return position + n
    else:
        return n + position - size


def increment(n, d):
    size = len(d)
    new = deque(-1 for x in range(size))
    for i in range(size):
        new[0] = d[i]
        new.rotate(-n)
        if new.count(-1) > 0:
            while new[0] != -1:
                new.rotate(-1)
    return new


def increment_card(position, n, size):
    return (position * n) % size


def increment_card_rev(position, n, size):
    return (-position * n) % size


def test_increment(n, d):
    d_size = len(d)
    rev_list = deque(-1 for x in range(d_size))
    for i, j in enumerate(d):
        np = (i * n) % d_size
        rev_list[np] = j
    return rev_list


def test_increment_rev(n, d):
    d_size = len(d)
    rev_list = deque(-1 for x in range(d_size))
    for i, j in enumerate(d):
        np = (i * n) % d_size
        rev_list[np] = j
    return rev_list


# print("Increment Reverse")
# print(deck)
# new_deck = increment(7, deck)
# print(new_deck)
# print(increment_card_rev(3, 7, 10))
#
# print("Cut Reverse")
# print(deck)
# new_deck = cut(7, deck)
# print(new_deck)
# print(cut_card_rev(9, 7, 10))

# print("Deal Reverse")
# print(deck)
# new_deck = deal(deck)
# print(new_deck)
# print(deal_card_rev(7, 10))


# for command in lines:
#     cs = command.split(" ")
#     if "increment" in cs:
#         i = int(cs[3]) % len(deck)
#         deck = increment(i, deck)
#     if "new" in cs:
#         deck = deal(deck)
#     if "cut" in cs:
#         c = int(cs[1]) % len(deck)
#         deck = cut(c, deck)
#
# print(deck)

#
#
# print(deck)
# print("Position: {}, Value: {}".format(pos, deck[pos]))
# # Testing
# for command in reversed(lines):
#     cs = command.split(" ")
#     if "increment" in cs:
#         pos = increment_card_rev(pos, int(cs[3]), deck_size)
#     if "new" in cs:
#         pos = deal_card_rev(pos, deck_size)
#     if "cut" in cs:
#         pos = cut_card_rev(pos, int(cs[1]), deck_size)
#
# print(deck)
# print("Position: {}, Value: {}".format(pos, deck[pos]))



# Part 1
# mods = [x % 10 for x in range(70, -56, -7)]
# print(mods)
# print(deck.index(2019))
# print(deck)

# Part 2
# deck_size = 119315717514047
# for n, c in enumerate(lines):
#     if n == 0:
#         continue
#     cs = c.split(" ")
#     pcs = lines[n-1].split(" ")
#     if "inc" in cs and "inc" in pcs:
#         lines[n-1] = "inc {}".format(int(pcs[1]) * int(cs[1]) * -1)
#         lines[n] = "inc {}".format(-1)

    # if "new" in cs:
    #     pos = deal_card_rev(pos, deck_size)
    # if "cut" in cs:
    #     pos = cut_card_rev(pos, int(cs[1]), deck_size)


# Can't do this for the whole deck, just need to follow a single card
deck_size = 119315717514047
pos = 4
for i in range(101741582076661):
    for command in lines:
        cs = command.split(" ")
        if "inc" in cs:
            pos = increment_card_rev(pos, int(cs[1]), deck_size)
        if "new" in cs:
            pos = deal_card_rev(pos, deck_size)
        if "cut" in cs:
            pos = cut_card_rev(pos, int(cs[1]), deck_size)

    assert(pos == 69824951015026)
    # assert(pos == -99059)
    print(pos)
    break

# pos = increment_card_rev(pos, 677511286858179345720242930801861539621459722240000000000000000000, deck_size)
# for x in range(-2000000, 2000000, 1):
#     this = cut_card_rev(pos, x, deck_size)
#     if this == 107979614696968:
#         print("Cut: {}".format(x))

