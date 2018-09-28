# Otis Scott
# CS - UY 1114
# 19 Sept 2018
# Lab 3
import math


def normaldist(x):
    lead = 1 / (math.sqrt(2 * math.pi))
    power = (-1/2) * x ** 2
    exp = math.pow(math.e, power)
    return lead * exp


print("The value of the pdf at x = 0.0 is " + str(normaldist(0)))
print("The value of the pdf at x = 1.0 is " + str(normaldist(1)))
print("The value of the pdf at x = -1.0 is " + str(normaldist(-1)))
