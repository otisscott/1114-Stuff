# Otis Scott
# CS - UY 1114
# 10 Oct 2018
# Homework 5

password = input("Enter a password: ")

dub_upper = 0
lower = False
dig_count = 0
special = False

for char in password:
    if char.isupper():
        dub_upper += 1
    elif char.islower():
        lower = True
    elif char.isdigit():
        dig_count += 1
    elif char in "!" "@" "#" "$":
        special = True

if lower and special and dub_upper >= 2 and dig_count >= 2 and len(password) >= 8:
    print(password + " is a valid password")
else:
    print(password + " is not a valid password")
