inp = int(input("Enter a positive integer: "))
for rows in range(inp):
    row = ""
    for columns in range(inp):
        if columns < rows:
            row += "#"
        elif rows < columns:
            row += "$"
        else:
            row += "%"
    print(row)
