sum1 = int(input("Enter the first number: "))
sum2 = int(input("Enter the second number: "))


def square_of_sum(num1, num2):
    """
    num1: int, num2: int, return: int
    """
    return (num1 + num2) ** 2


print(square_of_sum(sum1, sum2))
