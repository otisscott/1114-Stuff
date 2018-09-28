# Otis Scott
# CS - UY 1114
# 19 Sept 2018
# Homework 2

a_days = int(input("Please enter the number of days Alice has worked: ")) * 1440
a_hours = int(input("Please enter the number of hours Alice has worked: ")) * 60
a_minutes = int(input("Please enter the number of minutes Alice has worked: "))
b_days = int(input("Please enter the number of days Bob has worked: ")) * 1440
b_hours = int(input("Please enter the number of hours Bob has worked: ")) * 60
b_minutes = int(input("Please enter the number of minutes Bob has worked: "))

total_time = a_days + a_hours + a_minutes + b_days + b_hours + b_minutes
total_days = total_time // 1440
total_time_no_days = (total_time - (total_days * 1440))
total_hours = total_time_no_days // 60
minutes = (total_time_no_days - (total_hours * 60))

print("The total time both of them worked together is: " + str(total_days) + " days, " + str(total_hours) + \
      " hours and " + str(minutes) + " minutes.")
