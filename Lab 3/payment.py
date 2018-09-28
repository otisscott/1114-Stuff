# Otis Scott
# CS - UY 1114
# 27 Sept 2018
# Lab 4

fprice = float(input("Enter price of first item: "))
sprice = float(input("Enter price of second item: "))
card = input("Does customer have a club card? (Y/N): ")
tax = float(input("Enter tax rate, e.g. 5.5 for 5.5% tax: ")) / 100 + 1

print("Base price: " + str(fprice + sprice))

if fprice < sprice:
    fprice = fprice * 0.4
else:
    sprice = sprice * 0.4

if card == "Y":
    sprice = sprice * 0.9
    fprice = fprice * 0.9

print("Price after discounts: " + str(round(sprice + fprice, 2)))

print("Total price: " + str(round((sprice + fprice) * tax, 2)))
