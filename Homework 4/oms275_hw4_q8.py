# Otis Scott
# CS - UY 1114
# 4 Oct 2018
# Homework 4

for row in range(1, 6):
    row_str = ""
    for column in range(1, 11):
        row_str += str(column ** row) + "\t"
    print(row_str)
