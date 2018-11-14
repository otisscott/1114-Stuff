import turtle
import time


def loadpgm(filename):
    with open(filename, "r") as f:
        if f.readline().strip() != "P2":
            raise ValueError("Not a pgm file")
        dimensions = f.readline().strip().split()
        x = int(dimensions[0])
        y = int(dimensions[1])
        maxgrey = int(f.readline().strip())
        final = []
        for i in range(y):
            rowdata = f.readline().strip().split()
            for each in range(len(rowdata)):
                rowdata[each] = int(rowdata[each])
            final.append(rowdata)
        return final


def display(data):
    """
    sig: list(list(int)) -> NoneType
    Display grayscale pixel data on the turtle canvas
    """
    turtle.tracer(0,0)
    turtle.hideturtle()
    for irow in range(len(data)):
        for icol in range(len(data[irow])):
            val = data[irow][icol]
            turtle.up()
            turtle.goto(icol, -irow)
            turtle.down()
            turtle.color((val/255, val/255, val/255))
            turtle.dot(2)
        turtle.update()


def rotate(data):
    """
    sig: list(list(int)) -> list(list(int))
    Give grayscale pixel data, rotate the image
    by inverting the rows and columns. That is
    if the input is a 300x444 image, the result
    should be a 444x300 pixel image.
    The is a pure function; it returns a new
    image.
    """
    final = []
    for column in range(len(data[0])):
        row_list = []
        for row in range(len(data)):
            row_list.append(data[row][column])
        final.append(row_list)
    return final


def darken(data, quantity):
    """
    sig: list(list(int)), int -> NoneType
    Given grayscale pixel data, darken
    the image by the given number of shades
    This is a mutating function, changing
    the value of data
    """
    for row in range(len(data)):
        for column in range(len(data[row])):
            row[column] = row[column] - quantity
            if row[column] < 0:
                row[column] = 0
            elif row[column] > 255:
                row[column] = 255
    return data


nyc = loadpgm("nyc.pgm")
rotated = rotate(nyc)
display(rotated)
#print(nyc[0])
