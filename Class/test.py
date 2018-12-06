def less_than_10s(nums):
    initial = nums.copy()
    final = []
    for collection in initial:
        if sum(collection) < 10:
            final.append(collection)
    return final


def insert_at_each(nums, num):
    initial = nums.copy()
    for count in range(0, len(initial)):
        if count >= len(initial[count]):
            initial[count].append(num)
        else:
            initial[count][count] = num
    return initial


def first_instances_only(s):
    final = ""
    for each in s:
        if each not in final:
            final += each
    return final


def count_chars(inp):
    chars = list(inp)
    chars.sort()
    while " " in chars:
        chars.remove(" ")
    letters = []
    for char in chars:
        start = chars[0]
        count = chars.count(start)
        while start in chars:
            chars.remove(start)
        letters.append((start, count))
    return letters


def most_common(s):
    counted = count_chars(s)
    most = ("", 0)
    for tup in counted:
        if tup[1] > most[1]:
            most = tup
    return most[0]


def main():
    tens = less_than_10s([[5, 10], [1, 2, 3], [8, 1], [9, 1]])
    green_eggs = first_instances_only("Green eggs and spam")
    inserted = insert_at_each([[100, 200, 300], [400, 500, 600], [700], [800, 900, 1000]], 5)
    test_str = "This is a string"
    letter_count = count_chars(test_str)
    common = most_common(test_str)
    print(tens)
    print(green_eggs)
    print(inserted)
    print(letter_count)
    print(common)


main()
