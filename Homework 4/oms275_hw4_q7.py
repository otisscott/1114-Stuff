# Otis Scott
# CS - UY 1114
# 4 Oct 2018
# Homework 4

binar = input("Enter a binary number: ")
dec = 0
cnt = 0
for each in range(len(binar) - 1, -1, -1):
    dec += int(binar[each]) * 2 ** cnt
    cnt += 1

print("In decimal, that is " + str(dec))
