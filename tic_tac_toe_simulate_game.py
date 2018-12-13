import os
import sys

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import tensorflow as tf
import keras

from tqdm import tqdm

import random

choices = []

for k in range(9):

    choices.append(str(k))

player_1_moves = []
player_2_moves = []

admissible_choices = ['X', 'O']

feed_joe = []


def board():

    print('\n#######')
    print('|' + choices[0] + '|' + choices[1] + '|' + choices[2] + '|')
    print('|' + choices[3] + '|' + choices[4] + '|' + choices[5] + '|')
    print('|' + choices[6] + '|' + choices[7] + '|' + choices[8] + '|')
    print('#######\n')


def check_win_or_tie(player_wins, player, choices):

    assert player_wins == 0

    for z in range(3):

        l = z*3

        if (choices[l] == choices[l+1] == choices[l+2]) or (choices[z] == choices[z+3] == choices[z+6])\
                or (choices[0] == choices[4] == choices[8]) or (choices[2] == choices[4] == choices[6]):

            player_wins = 1
            print player, 'wins!'
            board()
            quit()

        else:
            player_wins = 0

    if any(item.isdigit() for item in choices) == 0:

        print 'The game is a tie!'
        board()
        quit()

    return player_wins


def random_bot(x_or_o, moves_already_made):

    possible_moves = tuple(i for i in moves_already_made if i not in x_or_o)

    decision = random.choice(possible_moves)

    return decision


def two_bots_marker(admissible_choices):

    bot1_marker = random.choice(admissible_choices)
    bot2_marker = str(tuple(i for i in admissible_choices if i != bot1_marker)[0])

    return bot1_marker, bot2_marker


def two_bots_turn(bot1_marker, bot2_marker, bot_wins):

    while bot_wins == 0:

        bot_move = random_bot(admissible_choices, choices)

        choices[int(bot_move)] = bot1_marker

        bot_wins = check_win_or_tie(bot_wins, 'Bot 1', choices)

        if bot_wins == 0:

            bot_move = random_bot(admissible_choices, choices)

            choices[int(bot_move)] = bot2_marker

            bot_wins = check_win_or_tie(bot_wins, 'Bot 2', choices)


bot1_XorO, bot2_XorO = two_bots_marker(admissible_choices)
player_wins = 0
two_bots_turn(bot1_XorO, bot2_XorO, player_wins)
