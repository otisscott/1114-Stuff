# Otis Scott
#CS - UY 1114
# 12 Sept 2018
# Homework 1

print("Please enter number of coins.")
quarters = int(input("Number of of quarters: "))
dimes = int(input("Number of of dimes: "))
nickels = int(input("Number of of nickels: "))
pennies = int(input("Number of of pennies: "))

total = 0.25 * quarters + 0.1 * dimes + 0.05 * nickels + 0.01 * pennies
dollar_total = int(total)
cent_total = total - dollar_total
cent_total = int(round(cent_total, 2) * 100)

print("The total is " + str(dollar_total) + " dollars and " + str(cent_total) + " cents")