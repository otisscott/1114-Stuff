# Otis Scott
# CS - UY 1114
# 10 Oct 2018
# Homework 5


def print_top (offset) :
    # signature: int -> NoneType
    print(offset * ' ' + '^')


def print_middle (offset , width) :
    # signature: int , int -> NoneType
    print(offset * ' ' + '/' + width * ' ' + '\\')


def print_bottom (offset , width):
    # signature: int , int -> NoneType
    print(offset * ' ' + width * '-')


def print_triangle():
    print_top(7)
    print_middle(6, 1)
    print_middle(5, 3)
    print_middle(4, 5)
    print_bottom(4, 7)


def rotate(s):
    """
    sig: str -> str
    Return the rotation of the given string
    rotate("spatula") == "patulas"
    """
    final = ""
    for each in range(1, len(s)):
        final += s[each]
    final += s[0]
    return final


def rotates(s, n):
    """
    sig: str, int -> str
    Return the nth rotation of the given string
    rotates("spatula", 0) == "spatula"
    rotates("spatula", 1) == "patulas"
    rotates("spatula", 2) == "atulasp"
    """
    for each in range(n):
        s = rotate(s)
    return s


def all_rotations(s):
    """
    sig: str -> NoneType
    Print all rotations of the given string
    all_rotations("far") should print these 3 lines:
    far
    arf
    rfa
    """
    for each in range(0, len(s)):
        print(rotates(s, each))


def double(n):
    # signature: int -> int
    # return doubled value of parameter
    return n * 2


def succ(n):
    # signature: int -> int
    # returns successor of parameter
    return n + 1


def f(n):
    # signature: int -> int
    # returns the value 2*n + 1
    return succ(double(n))


def g(n):
    # signature: int -> int
    # returns the value 4*n
    return double(double(n))


def h(n):
    # signature: int -> int
    # returns the value 8*n + 4
    return g(f(n))


def sum_range(start_num , end_num):
    """
    signature: int, int -> int
    precondition: end_num >= start_num
    Returns the sum of all numbers between start_num
    and end_num
    """
    final = 0
    for each in range(start_num, end_num + 1):
        final += each
    return final


def count_doubled(s):
    """
    signature: str -> int
    Returns the number of times that s
    contains a doubled character
    """
    count = 0
    for each in range(1, len(s)):
        if s[each] == s[each - 1]:
            count += 1
    return count


def main():
    print("Problem 2: ")
    print_triangle()
    print("Problem 3: all rotations of 'far'")
    all_rotations("far")
    print("Problem 4: All functions with 1 as input")
    print(f(1))
    print(g(1))
    print(h(1))
    print("Problem 5: sum of numbers between 1 and 11")
    print(sum_range(1, 11))
    print("Problem 6: foooff as the input")
    print(count_doubled("foooff"))


main()
