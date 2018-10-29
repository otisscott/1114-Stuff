# Otis Scott
# CS - UY 1114
# 19 Sept 2018
# Lab 4

import random

num1, num2, num3 = chr(random.randint(97, 122)), chr(random.randint(97, 122)), chr(random.randint(97, 122))
randstr1, randstr2, randstr3 = num1 + num2 + num3, num3 + num1 + num2, num2 + num3 + num1

print(randstr1)
print(randstr2 + " " + str(randstr1 > randstr2))
print(randstr3 + " " + str(randstr1 > randstr3))
