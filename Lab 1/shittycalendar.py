userDays = int(input("Please enter number of days:"))

weeks = str(userDays // 7)
days = str(userDays % 7)
userDays = str(userDays)

print(userDays + " days is equal to " + weeks + " week and " + days + " days")
