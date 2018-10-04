# Otis Scott
# CS - UY 1114
# 4 Oct 2018
# Homework 4

num = int(input("Enter a decimal number: "))
orig = num
roman = ""

if num > 1000:
    roman += "M" * (num // 1000)
    num = num % 10
if num > 500:
    roman += "D"
    num = 500
if num > 100:
    roman += "C" * (num // 100)
    num = num % 100
if num > 50:
    roman += "L"
    num -= 50
if num > 10:
    roman += "X" * (num // 10)
    num = num % 10
if num > 5:
    roman += "V"
    num -= 5
if num > 0:
    roman += "I" * num
    num = 0

print(str(orig) + " is " + roman)