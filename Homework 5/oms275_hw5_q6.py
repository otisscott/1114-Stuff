# Otis Scott
# CS - UY 1114
# 10 Oct 2018
# Homework 5

inp = input("Enter a mathematical expression: ")

first_space = inp.find(" ")
second_space = inp.find(" ", first_space + 1)
first = int(inp[0:first_space])
operator = inp[first_space + 1:second_space]
second = int(inp[second_space:len(inp)])

if operator == "+":
    print(inp + " = " + str(first + second))
elif operator == "-":
    print(inp + " = " + str(first - second))
elif operator == "*":
    print(inp + " = " + str(first * second))
elif operator == "/":
    print(inp + " = " + str(first / second))
