# Otis Scott
# CS - UY 1114
# 4 Oct 2018
# Homework 4

import random
num = random.randint(1, 100)
guess = 0
print(num)
print("I'm thinking of a number between 1 and 100, try to guess it.")
while guess != num:
    inp = input("Please enter a number between 1 and 100: ")
    if inp.isdigit():
        if 100 >= int(inp) >= 1:
            guess = int(inp)
            if guess > num:
                print("Your guess was too high, try again")
            elif guess < num:
                print("Your guess was too low, try again")
    else:
        print('Sorry but "' + str(inp) + '" is not a number between 1 and 100.')
print("Congradulations, you guessed the number!")
