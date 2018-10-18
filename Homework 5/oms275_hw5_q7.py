# Otis Scott
# CS - UY 1114
# 10 Oct 2018
# Homework 5

needle = input("Enter needle: ")
haystack = input("Enter haystack: ")
position = -1
for each in range(0, len(haystack) + 1 - len(needle)):
    if haystack[each:each + len(needle)] == needle:
        position = each
        break

if position == -1:
    print("Needle not found in haystack")
else:
    print("Needle found in haystack at position " + str(position))
