inp = input("Enter a string: ")

middle = len(inp) // 2
is_pal = True

for each in range(0, middle):
    if inp[each] != inp[-(each + 1)]:
        is_pal = False

if is_pal:
    print(inp + " is a palindrome")
else:
    print(inp + " is not a palindrome")
