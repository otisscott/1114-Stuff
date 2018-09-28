# Otis Scott
# CS - UY 1114
# 27 Sept 2018
# Lab 4

twentyfour = int(input("Please enter time in 24 hr format: "))
tfhours = twentyfour // 100
minutes = twentyfour % 100


if twentyfour // 100 < 12:
    if tfhours == 0:
        print(str(tfhours) + ":" + str(minutes) + " in 12 hr format is 12:" + str(minutes) + "am")
    else:
        print(str(tfhours) + ":" + str(minutes) + " in 12 hr format is " + str(tfhours) + ":" + str(minutes) + "am")
else:
    hours = twentyfour // 100 - 12
    if hours == 0:
        print(str(tfhours) + ":" + str(minutes) + " in 12 hr format is 12:" + str(minutes) + "pm")
    else:
        print(str(tfhours) + ":" + str(minutes) + " in 12 hr format is " + str(hours) + ":" + str(minutes) + "pm")
