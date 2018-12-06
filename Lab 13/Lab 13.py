class Calendar:
    def __init__(self):
        date = input("Please enter today's date in mm/dd/yy format: ").split("/")
        day = date[1]
        month = date[0]
        year = date[2]
        weekday = input("Please enter the day of the week today (1 for Monday and 7 for Sunday): ")
        self.day = int(day)
        self. month = int(month)
        self.year = int(year)
        self.weekday = int(weekday)
        self.to_do_list = ToDoList([])

    def __repr__(self):
        final = ""
        weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        final += "Today's date is: " + weekdays[self.weekday - 1] + " " + str(self.month) + "/" + str(self.day) + "/" + str(self.year) + "\n"
        final += self.to_do_list.__repr__()
        return final

    def start_new_day(self):
        month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.day + 1 > month_lengths[self.month - 1]:
            if int(self.month) == 12:
                self.month = 1
                self.day = 1
                self.year += 1
            else:
                self.month += 1
                self.day = 1
        else:
            self.day += 1
        if self.weekday >= 7:
            self.weekday = 1
        else:
            self.weekday += 1


class ToDoList:
    def __init__(self, tasks):
        self.tasks = tasks
        self.complete = []

    def create_to_do_list_item(self, task):
        self.tasks.append(task)
        self.complete.append(0)

    def check_to_do_list(self):
        for task in range(len(self.tasks)):
            if self.complete[task] == 0:
                is_complete = input("Did you complete: " + self.tasks[task] + "? ")
                if is_complete.lower() == "yes":
                    self.complete[task] = 1

    def __repr__(self):
        final = ""
        completed = ""
        incomplete = ""
        for task in range(len(self.tasks)):
            if self.complete[task] == 1:
                completed += self.tasks[task] + "\n"
            else:
                incomplete += self.tasks[task] + "\n"
        final += "Today's Accomplishments \n"
        final += "========================= \n"
        final += completed
        final += "Things Left To DO \n"
        final += "========================= \n"
        final += incomplete
        return final


def main():
    calendar = Calendar()
    while True:
        print("\n Main Menu :")
        print("1. Create New Calendar ")
        print("2. Add To - Do List Item ")
        print("3. Check Off To - Do List ")
        print("4. Show Today ’ s Calendar ")
        print("5. Start The Next Day \n ")
        answer = input(" What would you like to do? ")
        if answer == "1":
            calendar = Calendar()
        elif answer == "2":
            task = input("Enter the task: ")
            calendar.to_do_list.create_to_do_list_item(task)
        elif answer == "3":
            calendar.to_do_list.check_to_do_list()
        elif answer == "4":
            print(repr(calendar))
        elif answer == "5":
            calendar.start_new_day()


main()
