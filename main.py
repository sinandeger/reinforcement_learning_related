import os
import sys

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import tensorflow as tf
import keras

from tqdm import tqdm

import random

import multiplayer_tic_tac_toe as mp_game

choices = []

for k in range(9):

    choices.append(str(k))

player_1_moves = []
player_2_moves = []

admissible_choices = ['X', 'O']

print 'Welcome to this amazing implementation of the legendary game Tic-Tac-Toe!'

print "Please type choose 1 for a multiplayer game, 2 for a match against an algorithm that only makes random moves."


def game_type():

    game_choice = str(raw_input(">> "))

    if game_choice == '1':

        mp_game.MPTicTacToe()

    else:

        print 'Invalid selection.'
        print "Please type 1 for a multiplayer game, 2 for a match against an algorithm that only makes random moves."

        game_type()

game_type()


