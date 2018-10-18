num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

count = 0
for dig in range(0, len(num1)):
    if num1[dig] != num2[dig]:
        count += 1
print("The hamming Distance between " + num1 + " and " + num2 + " is " + str(count))
