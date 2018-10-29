inp = input("Enter a sequence of positive integers, each one on a separate line. \n "
            "End your sequence by typing -1: ")

count = 0


while int(inp) != -1:
    check = True
    for each in range(1, len(inp), 1):
        if inp[0] != inp[each]:
            check = False
    if check:
        count += 1
    inp = input()

print("You entered " + str(count) + " mono-digit numbers")
