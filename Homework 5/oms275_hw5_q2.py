# Otis Scott
# CS - UY 1114
# 10 Oct 2018
# Homework 5

initial = input("Enter a string: ")
final = ""

for each in initial:
    if each == " ":
        final += "_"
    else:
        final += each

print(final)
