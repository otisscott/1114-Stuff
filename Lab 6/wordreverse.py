inp = input("Enter a line of text: ")
final = ""
last_space = -1
for char in range(0, len(inp)):
    if inp[char] == " ":
        for each in range(char - 1, last_space, -1):
            final += inp[each]
        final += " "
        last_space = char
    elif char == len(inp) - 1:
        for each in range(char, last_space - 1, -1):
            final += inp[each]
print(final)
