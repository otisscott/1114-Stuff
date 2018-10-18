# Otis Scott
# CS - UY 1114
# 10 Oct 2018
# Homework 5

inp = input("Enter a string: ")
final = ""

for letter in range(0, len(inp)):
    if inp[letter - 1] == " " or letter == 0:
        final += inp[letter].upper()
    else:
        final += inp[letter]

print(final)
