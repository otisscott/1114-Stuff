# Otis Scott
# CS - UY 1114
# 4 Oct 2018
# Homework 4

num = int(input("Enter a decimal number: "))
number = num
orig = num
count = 0
bin = ""

while num != 0:
    num = num // 2
    count += 1

for each in range(count - 1, -1, -1):
    if (number - 2 ** each) >= 0:
        bin += "1"
        number -= 2 ** each
    else:
        bin += "0"

print("The binary representation of " + str(orig) + " is " + str(bin))
