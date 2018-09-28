year = int(input("Enter a year: "))
print(str(year) + " is a leap year" if year % 400 == 0 and year % 100 == 0 or year % 4 == 0 and year % 100 != 0 else str(year) + " is not a leap year")
