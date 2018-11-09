# Otis Scott
# CS - UY 1114
# 5 Nov 2018
# Homework 7


def avg(numbers):
    """
    signature: list (float) -> float
    precondition: numbers != []
    returns the average (mean) of a non-empty list of floats
    """
    average = 0
    for digit in numbers:
        average += digit
    average = average / len(numbers)
    return average


def sum_some(lower, upper, numbers):
    up = 0
    lw = 0
    total = 0
    if not numbers:
        return 0
    else:
        if upper not in numbers:
            up = numbers[len(numbers) - 1]
        else:
            up = len(numbers) - numbers[::-1].index(upper)
        if lower > numbers[0]:
            lw = numbers.index(lower)
        for digit in range(lw, up):
            total += numbers[digit]
    return total


def is_sorted(my_list):
    sorted_list = my_list.copy()
    sorted_list = sorted(sorted_list)
    if my_list == sorted_list:
        return True
    return False


def indices(needle, haystack):
    final = []
    for each in range(0, len(haystack)):
        if haystack[each] == needle:
            final.append(each)
    return final


def intersperse():
    sentence1 = input("Enter a sequence: ")
    sentence2 = input("Enter a sequence: ")
    big_list = [sentence1.split(" "), sentence2.split(" ")]
    final = []
    for index in range(0, max(len(lists) for lists in big_list)):
        if index < len(big_list[0]):
            final.append(big_list[0][index])
        if index < len(big_list[1]):
            final.append(big_list[1][index])
    return " ".join(final)


def rlencode(s):
    """
    signature: str -> list(tuple(str, int))
    """
    count = 0
    final = []
    for char in range(0, len(s)):
        if char == len(s) - 1:
            if s[char - 1] == s[char]:
                count += 1
                final.append((s[char], count))
            else:
                final.append((s[char], 1))
        elif s[char] == s[char + 1]:
            count += 1
        else:
            count += 1
            final.append((s[char], count))
            count = 0
    return final


def rldecode(rle):
    """
    signature: list(tuple(str, int)) -> str
    """
    final = ""
    for each in range(0, len(rle)):
        final += rle[each][0] * rle[each][1]
    return final


def reverse_pure(xs):
    """
    signature: list(int) -> list(int)
    Returns a list of integers in reverse order
    """
    list_copy = xs.copy()
    reversed_list = []
    for index in range(len(list_copy) - 1, -1, -1):
        reversed_list.append(list_copy[index])
    return reversed_list


def reverse_mut(xs):
    """
    signature: list(int) -> NoneType
    Reverses the list of integers in place
    """
    list_copy = xs
    counter = 0
    for index in range(len(list_copy) - 1, -1, -1):
        xs[counter] = list_copy[index]
        counter += 1


def main():
    print("Problem 2:")
    print(avg([5, 43, 82, 7]))
    print("Problem 3:")
    print(sum_some(0, 100, []))
    print(sum_some(0, 100, [1, 2, 3, 4, 5]))
    print(sum_some(2, 4, [1, 2, 3, 4, 5]))
    print(sum_some(3, 3, [2, 2, 3, 3, 4, 4]))
    print("Problem 4:")
    print(is_sorted([]))
    print(is_sorted([1]))
    print(is_sorted([1, 2, 3]))
    print(is_sorted([1, 2, 2, 3]))
    print(is_sorted([1, 2, 2, 1]))
    print("Problem 5:")
    print(indices(7, []))
    print(indices(7, [6]))
    print(indices(7, [7, 8, 9]))
    print(indices(7, [1, 7, 7, 6]))
    print(indices(7, [0, 7, 1, 7, 2, 7, 3]))
    print("Problem 6: ")
    print(intersperse())
    print(rlencode("aadccccaa"))
    print(rldecode(rlencode("aadccccaa")))
    print("Problem 7: ")
    mylist = [5, 12, 34, 0, 1]
    newlist = reverse_pure(mylist)
    print(newlist)
    print(mylist)
    reverse_mut(mylist)
    print(mylist)


main()
