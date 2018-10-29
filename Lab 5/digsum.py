# Otis Scott
# CS - UY 1114
# 4 Oct 2018
# Homework 4

num = int(input("Enter a positive integer: "))
total = 0

for each in range(1, len(str(num))):
    total += num // (each * 10) % 10

print(total)
