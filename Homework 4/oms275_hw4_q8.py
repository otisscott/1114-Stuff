# Otis Scott
# CS - UY 1114
# 4 Oct 2018
# Homework 4

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for column in range(1, 6):
    row_str = ""
    for row in range(0, len(arr)):
        row_str += str(arr[row] ** column) + " \t"
    print(row_str)
