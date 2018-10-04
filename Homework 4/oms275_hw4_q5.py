# Otis Scott
# CS - UY 1114
# 4 Oct 2018
# Homework 4

size = int(input("Enter the size of the starting line: "))
is_even = -1

for each in range(size, 0, -2):
    print(" " * ((size - each) // 2) + '*' * each)

if size % 2 == 0:
    is_even = 2

for each in range(is_even, size + 1, 2):
    print(" " * ((size - each) // 2) + '*' * each)
