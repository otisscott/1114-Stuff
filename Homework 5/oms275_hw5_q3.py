# Otis Scott
# CS - UY 1114
# 10 Oct 2018
# Homework 5

inp = input("Enter a string: ")
check = False

for letter in inp:
    if letter == "'" "." "," ";" ":" "?" "!":
        check = True
        break

if check:
    print("That string does contain punctuation")
else:
    print("That string does contain punctuation")
