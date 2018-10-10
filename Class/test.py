s = input("Enter a string: ")
i = 0
acc = ""
while i < len(s):
    acc = s[i] + acc
    i += 1
print(acc)
