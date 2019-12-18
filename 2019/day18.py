import aoc_common as ac

pos = 0 + 0j
room = {pos: "."}

turn_right = {
    "north": "east",
    "south": "west",
    "east": "south",
    "west": "north"
}

turn_left = {
    "north": "west",
    "south": "east",
    "east": "north",
    "west": "south"
}

directions = {
    "north": 1,
    "south": 2,
    "east": 3,
    "west": 4
}

movement = {
    "north": 0 + 1j,
    "south": 0 - 1j,
    "east": 1 + 0j,
    "west": -1 + 0j
}

p