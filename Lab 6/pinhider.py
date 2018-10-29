inp = input("Enter a line of text: ")
final = ""
last_space = 0
for char in range(0, len(inp)):
    if inp[char] == " ":
        last_space = char
    if inp[char].isdigit() and not inp[last_space + 1:char - 1].isalpha():
        final += "x"
    else:
        final += inp[char]
print(final)
