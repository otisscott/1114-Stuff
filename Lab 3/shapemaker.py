# Otis Scott
# CS - UY 1114
# 27 Sept 2018
# Lab 4

sides = int(input("Enter the number of sides: "))

if sides == 3:
    equallen = int(input("How many sides are of equal length? "))
    lrgdegree = int(input("What is the degree of the largest angle of the triangle?"))
    if equallen == 3:
        print("The shape is an equilateral triangle")
    elif equallen == 2:
        if lrgdegree == 90:
            print("The shape is an isosceles right triangle")
        elif lrgdegree > 90:
            print("The shape is an isosceles obtuse triangle")
        else:
            print("The shape is an isosceles acute triangle")
    elif lrgdegree == 90:
        print("The shape is a right triangle")
    elif lrgdegree > 90:
        print("The shape is an obtuse triangle")
    else:
        print("The shape is an acute triangle")

if sides == 4:
    isequallen = input("Are the opposite sides equal in length? (Y/N): ")
    if isequallen == "Y":
        isninety = input("Are the angles all 90 degrees? (Y/N): ")
        if isninety == "Y":
            issquare = input("Are all sides equal? (Y/N): ")
            if issquare == "Y":
                print("The shape is a square")
            else:
                print("The shape is a rectangle")
        else:
            print("The shape is a paralellogram")
    else:
        print("The shape is a quadrilateral")
