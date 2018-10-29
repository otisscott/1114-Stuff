# Otis Scott
# CS - UY 1114
# 4 Oct 2018
# Homework 4

num = int(input("Enter a decimal number: "))
orig = num
roman = ""
while num > 0:
    if num > 1000:
        roman += "M"
        num -= 1000
    elif num > 500:
        roman += "D"
        num -= 500
    elif num > 100:
        roman += "C"
        num -= 100
    elif num > 50:
        roman += "L"
        num -= 50
    elif num > 10:
        roman += "X"
        num -= 10
    elif num > 5:
        roman += "V"
        num -= 5
    elif num > 0:
        roman += "I"
        num -= 1

print(str(orig) + " is " + roman)
