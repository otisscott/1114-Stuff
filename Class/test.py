def go(from_num, to_num):
    if to_num < from_num:
        temp = to_num
        to_num = from_num
        from_num = temp
    while from_num < to_num:
        print(str(from_num) + ".." + str(to_num))
        from_num += 1
        to_num -= 1


go(5, 10)
go(72, 69)
