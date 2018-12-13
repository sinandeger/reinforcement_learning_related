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


class MPTicTacToe:

    def __init__(self):

        self.admissible_choices = ['X', 'O']

        self.board()
        p1_marker, p2_marker, first_turn_choices = self.first_turn(self.admissible_choices)
        player_wins = 0
        self.not_first_turn(p1_marker, p2_marker, player_wins)

    def board(self):

        print('\n#######')
        print('|' + choices[0] + '|' + choices[1] + '|' + choices[2] + '|')
        print('|' + choices[3] + '|' + choices[4] + '|' + choices[5] + '|')
        print('|' + choices[6] + '|' + choices[7] + '|' + choices[8] + '|')
        print('#######\n')

    def check_win_or_tie(self, player_wins, player, choices):

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

    def move(self, player_marker):

        print "Please select the tile your marker, " + str(player_marker) + ", is to be placed"
        tile = str(raw_input(">> "))

        if tile in choices:
            choices[int(tile)] = player_marker
            self.board()

        else:
            print 'Incorrect tile selection, please choose an unoccupied tile between 1 and 9.'
            self.move(player_marker)

    def first_turn(self, admissible_choices):

        print 'Player 1: Please select X or O for your marker'

        p1_marker = str(raw_input(">> "))
        p2_marker = str(tuple(i for i in admissible_choices if i != p1_marker)[0])

        if p1_marker in admissible_choices:

            print "Player 1: You've selected", p1_marker

            self.move(p1_marker)
            self.board()

            print "Player 2 gets marker", p2_marker

            self.move(p2_marker)
            self.board()

        else:
            print 'Invalid marker selection.'
            self.first_turn()

        return p1_marker, p2_marker, choices

    def not_first_turn(self, p1_marker, p2_marker, player_wins):

        while player_wins == 0:

            print 'Player 1:'
            self.move(p1_marker)
            player_wins = self.check_win_or_tie(player_wins, 'Player 1', choices)

            if player_wins == 0:

                print 'Player 2:'
                self.move(p2_marker)
                player_wins = self.check_win_or_tie(player_wins, 'Player 2', choices)

