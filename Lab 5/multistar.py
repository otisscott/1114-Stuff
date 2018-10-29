# Otis Scott
# CS - UY 1114
# 4 Oct 2018
# Homework 4

import turtle
import time

times = int(input("How many stars: "))
times = times * 5

length = 20
angle = 144

for each in range(0, times):
    turtle.forward(length)
    turtle.right(angle)
    length += 10

time.sleep(5)
