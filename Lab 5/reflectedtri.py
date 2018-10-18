n = int(input("Enter a positive integer, n: "))
start = int(input("Enter a positive integer for starting value: "))

for rows in range(start - 1, start + n, 1):
    row = ""
    for column in range(rows - start + 1):
        row += str(rows)
    print(row)

for rows in range(start + n - 2, start - 1, -1):
    row = ""
    for column in range(rows - start + 1):
        row += str(rows)
    print(row)
