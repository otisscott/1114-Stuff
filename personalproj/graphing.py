import turtle
import math


func = input("please enter your function: ")

for x in range(-100, 100):
    new_func = ""
    for num in range(len(func)):
        if func[num] == "x":
            new_func += str(x/10)
        else:
            new_func += func[num]

    y = eval(func)
    turtle.setposition(x/10, y)
