inp = input("Enter a string of 0's and 1's: ")
print("Your string has: ")
count = 0
for dig in range(0, len(inp)):
    if dig == len(inp) - 1:
        if inp[dig] == inp[dig - 1]:
            count += 1
            print(str(count) + " " + inp[dig] + "'s")
        else:
            count += 1
            print(str(count) + " " + inp[dig] + "'s")
    elif inp[dig] == inp[dig + 1]:
        count += 1
    else:
        count += 1
        print(str(count) + " " + inp[dig] + "'s")
        count = 0
