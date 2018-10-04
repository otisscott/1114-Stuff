# Otis Scott
# CS - UY 1114
# 4 Oct 2018
# Homework 4

num = int(input("Enter a positive integer: "))
final = "1 "
last = 1
second = 0

for each in range(0, num):
    final += str(last + second) + " "
    second, last = last, last + second

print(final)
