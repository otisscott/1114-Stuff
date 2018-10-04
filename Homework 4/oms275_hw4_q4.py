# Otis Scott
# CS - UY 1114
# 4 Oct 2018
# Homework 4

import turtle
import time

sides = int(input("Enter the sides of the shape: "))
size = int(input("Enter the length of the sides: "))
angle = ((sides - 2) * 180)/sides

for each in range(0, sides):
    turtle.forward(size)
    turtle.right(180-angle)

time.sleep(5)
