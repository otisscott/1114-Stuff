def consecutive_numbers(filename, n):
    """
    sig : str , int -> NoneType
    """
    file = open(filename, "w+")
    for digit in range(0, n + 1):
        file.write(str(digit) + "\n")


def squared_numbers(filename, outFile):
    """
    sig : str , str -> NoneType
    """
    num_list = []
    with open(filename) as inp:
        num_list = inp.readlines()
    num_list = [this.strip("\n") for this in num_list]
    new_file = open(outFile, "w+")
    for index in range(0, len(num_list)):
        new_file.write(str(int(num_list[index]) ** 2) + "\n")


final_file = open("final_world.txt", "w+")


def parser():
    initial_world = []
    final_file.write("Generation 0 \n")
    with open('initial_world.txt') as text_input:
        initial_world = text_input.readlines()
    initial_world = [this.strip("\n") for this in initial_world]
    for string in range(0, len(initial_world)):
        final_file.write(initial_world[string] + "\n")
        initial_world[string] = initial_world[string].split(" ")
    return initial_world


def create_world(initial_world):
    starting_grid = []
    for column in range(0, 12):
        inner_list = []
        for row in range(0, 12):
            inner_list.append(0)
        starting_grid.append(inner_list)
    for column in range(0, 10):
        for row in range(0, 10):
            if initial_world[row][column] == "*":
                starting_grid[row + 1][column + 1] = 1
    return starting_grid


def checker(grid):
    new_grid = []
    for row in range(1, 11):
        row_list = []
        for column in range(1, 11):
            live_count = 0
            for horiz in range(-1, 2):
                for vert in range(-1, 2):
                    if not (row + horiz == row and column + vert == column):
                        if grid[row + horiz][column + vert] == 1:
                            live_count += 1
            if grid[row][column] == 0 and live_count == 3:
                row_list.append("*")
            elif grid[row][column] == 1 and live_count < 2:
                row_list.append("-")
            elif grid[row][column] == 1 and live_count > 3:
                row_list.append("-")
            elif grid[row][column] == 1:
                row_list.append("*")
            else:
                row_list.append("-")
        new_grid.append(row_list)
    return new_grid


def printer():
    grid = parser()
    new_grid = grid
    for trials in range(1, 11):
        grid = create_world(new_grid)
        new_grid = checker(grid)
        final_file.write("Generation " + str(trials) + "\n")
        for row in range(0, 10):
            inner_grid = ""
            for column in range(0, 10):
                inner_grid += new_grid[row][column] + " "
            final_file.write(inner_grid + "\n")


def main():
    consecutive_numbers('numbers.txt', 5)
    squared_numbers('numbers.txt', 'num_squared.txt')
    printer()


main()