#!../venv/bin/python3

import day9_input as d9
import aoc_common
from blist import blist


def play_the_game(player_toggle, marbles):
    player = next(player_toggle)
    the_game = [0, 1]
    the_game = blist(the_game)
    the_game_length = 1
    where_to_place = 1
    score = {}
    get = score.get

    # while marbles:
    for marble in marbles:
        the_game_length += 1
        player = next(player_toggle)
        if marble % 23 == 0:
            if where_to_place < 9:
                where_to_place = the_game_length + (where_to_place - 9)
                the_game_length -= 2
            else:
                where_to_place = where_to_place - 9
                the_game_length -= 2

            bonus = the_game[where_to_place]
            del the_game[where_to_place]
            score[player] = get(player, 0) + marble + bonus
            where_to_place += 2
        else:
            if where_to_place <= len(the_game):
                the_game.insert(where_to_place, marble)
                where_to_place += 2
            else:
                the_game.insert(1, marble)
                where_to_place = 3
    print(aoc_common.get_max_value_of_dictionary(score))


if __name__ == '__main__':
    # play_the_game(d9.player_toggle, d9.marble_iterator)
    print(play_the_game(d9.player_toggle, d9.part_two_marble_iterator))
