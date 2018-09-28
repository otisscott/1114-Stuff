# Otis Scott
# CS - UY 1114
# 26 Sept 2018
# Homework 3

import math

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

discriminant = b ** 2 - (4 * a * c)

if discriminant > 0:
    solution1 = (-b + math.sqrt(discriminant)) / 2 * a
    solution2 = (-b - math.sqrt(discriminant)) / 2 * a
    print("This equation has two real solutions: x = " + str(round(solution1, 1)) + " and x = " +
          str(round(solution2, 1)))
elif discriminant == 0:
    solution1 = -b / 2 * a
    print("This equation has a single real solution: x = " + str(round(solution1, 1)))
else:
    print("This equation has no real solutions")
