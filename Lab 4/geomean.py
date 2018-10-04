# Otis Scott
# CS - UY 1114
# 4 Oct 2018
# Homework 4

import math

start = int(input("Please enter a non - empty sequence of positive integers , each one on a separate line. \n "
                  "End your sequence by typing -1: "))
prod = 1
cnt = 0

while start > -1:
    prod *= start
    start = int(input())
    cnt += 1


mean = math.pow(prod, 1/cnt)

print("The geometric mean is: " + str(mean))
