inp = int(input("Enter a positive integer: "))
for counter in range(1, inp + 1, 1):
    row = ""
    for each in range(inp, 0, -1):
        if each > counter:
            row += "."
        else:
            row += str(counter)
    print(row)
