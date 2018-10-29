import math


def make_alpha_string(ch, n):
    final = ""
    start = ord(ch)
    for each in range(n):
        final += chr(start + each)
        if start + each >= 122:
            start = 96 - each
    return final


def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False


def print_n_ints(start, n):
    for each in range(n):
        print(start + each)


def print_shifted_triangle(lines, offset, symbol):
    for line in range(lines):
        row = (offset + (lines - line - 1)) * " " + (line * 2 + 1) * symbol
        print(row)


def print_pine_tree(num_triangles, symbol):
    for tri in range(num_triangles):
        lines = tri + 2
        offset = num_triangles - tri - 1
        print_shifted_triangle(lines, offset, symbol)


def print_month_calendar(num_days, start_day):
    weeks = (num_days + start_day) / 7
    weeks = math.ceil(weeks)
    print("Mon \t Tue \t Wed \t Thu \t Fri \t Sat \t Sun")
    week = " \t " * start_day
    count = start_day + 1
    for day in range(1, num_days + 1):
        if count > 7:
            print(week)
            week = ""
            count = 1
        week += str(day) + " \t "
        count += 1
        if day == num_days:
            print(week)
            return count - 1


def print_year_calendar(year, start_day):
    print("\n January " + str(year))
    jan_end = print_month_calendar(31, start_day - 1)
    print("\n February " + str(year))
    if is_leap_year(year):
        feb_end = print_month_calendar(29, jan_end)
    else:
        feb_end = print_month_calendar(28, jan_end)
    print("\n March " + str(year))
    mar_end = print_month_calendar(31, feb_end)
    print("\n April " + str(year))
    apr_end = print_month_calendar(30, mar_end)
    print("\n May " + str(year))
    may_end = print_month_calendar(31, apr_end)
    print("\n June " + str(year))
    jun_end = print_month_calendar(30, may_end)
    print("\n July " + str(year))
    jul_end = print_month_calendar(31, jun_end)
    print("\n August " + str(year))
    aug_end = print_month_calendar(31, jul_end)
    print("\n September " + str(year))
    sep_end = print_month_calendar(30, aug_end)
    print("\n October " + str(year))
    oct_end = print_month_calendar(31, sep_end)
    print("\n November " + str(year))
    nov_end = print_month_calendar(30, oct_end)
    print("\n December " + str(year))
    print_month_calendar(31, nov_end)


def main():
    print(make_alpha_string('a', 5))
    print(make_alpha_string('x', 6))
    print(is_leap_year(2016))
    print(is_leap_year(2018))
    print_n_ints(5, 6)
    print_n_ints(-3, 5)
    print_pine_tree(5, '#')
    print_year_calendar(2016, 6)


main()
