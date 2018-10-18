name1 = input("Enter name 1 in the format Last_Name, First_Name: ")
name2 = input("Enter name 2 in the format First_Name Last_Name: ")

space_place = 0
for each in range(len(name2)):
    if name2[each] == " ":
        space_place = each
first_check = name1.find(name2[0:space_place - 1]) > -1
last_check = name1.find(name2[space_place + 1:len(name2)])
if first_check > last_check > -1:
    print("The two names are equal!")
else:
    print("The two names are not equal")
