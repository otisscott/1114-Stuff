num = int(input("Enter a positive integer: "))
sum = 0
start = -11

for each in range(0, num):
    sum += start
    start += 3

print("The sum of the first " + str(num) + " terms of the sequence is " + str(sum))