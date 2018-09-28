import datetime

user_birth = input("Please input your DOB in yyyymmdd format: ")
current_time = datetime.datetime.now().strftime("%Y%m%d")

time_alive = int(current_time) - int(user_birth)
year_alive = time_alive // 10000
month_alive = time_alive // 100 % 100
day_alive = time_alive % 100

print("Date of birth is %s/%s/%s" % (user_birth[4:6], user_birth[6:len(user_birth)], user_birth[0:4]))
print("Current date is %s/%s/%s" % (current_time[4:6], current_time[6:len(current_time)], current_time[0:4]))
print("You have been alive for " + str(year_alive) + " years " + str(month_alive) + " months(s) and " + str(day_alive) + "day(s)")
