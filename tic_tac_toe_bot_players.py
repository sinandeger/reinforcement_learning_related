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


def board():

    print('\n#######')
    print('|' + choices[0] + '|' + choices[1] + '|' + choices[2] + '|')
    print('|' + choices[3] + '|' + choices[4] + '|' + choices[5] + '|')
    print('|' + choices[6] + '|' + choices[7] + '|' + choices[8] + '|')
    print('#######\n')


def who_goes_first():

    print 'Time for a digitized coin toss to determine who goes first! Heads or Tails?'

    toss = str(raw_input(">> "))

    heads_tails = ['Heads', 'Tails']

    outcome = random.choice(heads_tails)

    if toss == outcome:

        print str(outcome)+'! You go first!'
        return 'Player'

    else:

        print str(outcome)+'! Tic-Tac-Bot goes first!'
        return 'Bot'


def move(player_marker):

    print "Please select the tile your marker, " + str(player_marker) + ", is to be placed"
    tile = str(raw_input(">> "))

    if tile in choices:
        choices[int(tile)] = player_marker
        board()

    else:
        print 'Incorrect tile selection, please choose an unoccupied tile between 1 and 9.'
        move(player_marker)


def random_bot(x_or_o, moves_already_made):

    possible_moves = tuple(i for i in moves_already_made if i not in x_or_o)

    decision = random.choice(possible_moves)

    return decision


def versus_bot_first_turn(admissible_choices):

    first_move = who_goes_first()

    if first_move == 'Player':

        print 'Player 1: Please select X or O for your marker'

        p1_marker = str(raw_input(">> "))
        bot_marker = str(tuple(i for i in admissible_choices if i != p1_marker)[0])

        if p1_marker in admissible_choices:
            print "Player 1: You've selected", p1_marker

            move(p1_marker)
            board()

            print 'Tic-Tac-Bot has selected', bot_marker

            bot_move = random_bot(admissible_choices, choices)

            choices[int(bot_move)] = bot_marker
            board()

            return p1_marker, bot_marker, choices, first_move

    if first_move == 'Bot':

        bot_marker = random.choice(admissible_choices)
        p1_marker = str(tuple(i for i in admissible_choices if i != bot_marker)[0])

        print 'Tic-Tac-Bot has selected', bot_marker

        bot_move = random_bot(admissible_choices, choices)

        choices[int(bot_move)] = bot_marker
        board()

        print 'Your marker is', p1_marker

        move(p1_marker)
        board()

        return p1_marker, bot_marker, choices, first_move


def check_win_or_tie(player_wins, player, choices):

    assert player_wins == 0

    for z in range(3):

        l = z*3

        if (choices[l] == choices[l+1] == choices[l+2]) or (choices[z] == choices[z+3] == choices[z+6])\
                or (choices[0] == choices[4] == choices[8]) or (choices[2] == choices[4] == choices[6]):

            player_wins = 1
            print player, 'wins!'
            quit()

        else:
            player_wins = 0

    if any(item.isdigit() for item in choices) == 0:

        print 'The game is a tie!'
        quit()

    return player_wins


def versus_bot_not_first_turn(p1_marker, bot_marker, player_wins, first_move):

    while player_wins == 0:

        if first_move == 'Player':

            move(p1_marker)
            board()

            player_wins = check_win_or_tie(player_wins, 'Human player', choices)

            if player_wins == 0:

                bot_move = random_bot(admissible_choices, choices)
                choices[int(bot_move)] = bot_marker
                board()

                player_wins = check_win_or_tie(player_wins, 'Bot', choices)

        if first_move == 'Bot':

            bot_move = random_bot(admissible_choices, choices)
            choices[int(bot_move)] = bot_marker
            board()

            player_wins = check_win_or_tie(player_wins, 'Bot', choices)

            if player_wins == 0:

                move(p1_marker)
                board()

                player_wins = check_win_or_tie(player_wins, 'Human player', choices)


board()
p1_marker, bot_marker, first_turn_choices, first_move = versus_bot_first_turn(admissible_choices)
player_wins = 0
versus_bot_not_first_turn(p1_marker, bot_marker, player_wins, first_move)



