"""def word_count(text):
    dict1 = {}
    text_lst = text.lower().strip().replace('?', "").replace("!", "").split(" ")
    for word in text_lst:
        if word in dict1:
            dict1[word] += 1
        else:
            dict1[word] = 1
    return dict1


def main():
    print(word_count("I'm nobody! Who are you? Are you nobody, too? Then there's a pair of us - don't tell! They'd advertise - you know! How dreary to be somebody! How public like a frog To tell one's name the livelong day To an admiring bog!"))


main()
"""

class FuelTank():

    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.gallons = 0

    def __str__(self):
        return "The tank has a capacity of " + str(self.capacity) + ", and current has " + str(self.gallons) + " of fuel in it"

    def fill(self, gallons_in):
        self.gallons += gallons_in

    def is_empty(self):
        if self.gallons == 0:
            return True
        return False

    def get_percentage_full(self):
        return (self.gallons/self.capacity) * 100

    def use_fuel(self, rate_per_hour, hours):
        if self.gallons - (hours * rate_per_hour) <= 0:
            raise ValueError("There is not enough fuel left to do this")
        else:
            self.gallons -= hours * rate_per_hour


def main():
    tank1 = FuelTank(10)
    print(tank1.is_empty())
    tank1.fill(7)
    print(tank1.get_percentage_full())
    tank1.fill(12)
    print(tank1.get_percentage_full())
    tank1.use_fuel((0.5, 21))


main()