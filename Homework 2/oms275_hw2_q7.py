# Otis Scott
# CS - UY 1114
# 19 Sept 2018
# Homework 2

def bmi(w, h):
    bmi = w / h ** 2
    return bmi

weight = int(input("Please enter weight in kilograms: "))
height = float(input("Please enter height in meters: "))
print("BMI is: " + str(bmi(weight, height)))

pweight = int(input("Please enter weight in pounds: ")) * 0.453592
iheight = int(input("Please enter height in inches: ")) * 0.0254
print("BMI is: " + str(bmi(pweight, iheight)))

