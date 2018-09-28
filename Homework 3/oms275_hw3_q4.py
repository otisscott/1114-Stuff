# Otis Scott
# CS - UY 1114
# 26 Sept 2018
# Homework 3

import random

moves = ["rock", "paper", "scissors"]

computer_move = random.randint(0, 2)
player_move = moves.index(input("Please enter rock, paper, or scissors: "))
print("Computer selected: " + moves[computer_move])

if computer_move == player_move:
    print("Both players choose " + moves[computer_move] + ": No winner")
elif player_move == 0 and computer_move == 2 or player_move == 1 and computer_move == 0 or player_move == 2 and \
computer_move == 1:
    print(moves[player_move][0].upper() + moves[player_move][1:len(moves[player_move])] + " beats " +
          moves[computer_move] + ": You win!")
else:
    print(moves[computer_move][0].upper() + moves[computer_move][1:len(moves[computer_move])] + " beats " +
          moves[player_move] + ": You lose!")
