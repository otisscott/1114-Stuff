inp = int(input("Enter a positive integer, n: "))
for each in range(1, inp + 1, 1):
    counter = 0
    num = each
    digits = 0
    while num:
        if (num % 10) % 2 == 0:
            counter += 1
        num = num // 10
        digits += 1
    if counter > (digits / 2):
        print(each)
