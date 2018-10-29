# Otis Scott
# CS - UY 1114
# 27 Sept 2018
# Lab 5

import turtle
import time

distance = 100
interior_angles = 60
corner_angle = 120


def left_right():
    turn = input("Please enter 'R' for 'Right' or 'L' for 'Left': ")
    if turn == "R":
        turtle.right(interior_angles)
        turtle.forward(distance)
        turtle.right(corner_angle)
        turtle.forward(distance)
        turtle.right(corner_angle)
        turtle.forward(distance)
    elif turn == "L":
        turtle.left(-interior_angles)
        turtle.forward(distance)
        turtle.left(-corner_angle)
        turtle.forward(distance)
        turtle.left(-corner_angle)
        turtle.forward(distance)
    else:
        print("That value was not correct, try again")
        left_right()


left_right()
time.sleep(5)
