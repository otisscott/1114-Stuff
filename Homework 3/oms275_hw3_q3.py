# Otis Scott
# CS - UY 1114
# 26 Sept 2018
# Homework 3

days = ["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"]
rate = 0

day = days.index(input("Enter the day the call started: "))
time = int(input("Enter the time the call was started at (hhmm)"))
duration = int(input("Enter the duration of the call (in minutes)"))

if 0 <= day <= 4:
    if 800 <= time <= 1800:
        rate = 0.4
    else:
        rate = 0.25
else:
    rate = 0.15

cost = round(rate * duration, 2)

print("This call will cost $" + str(cost))