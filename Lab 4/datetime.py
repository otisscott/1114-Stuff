# Otis Scott
# CS - UY 1114
# 27 Sept 2018
# Lab 5

import datetime

curr_year = 2018

name = input("Please enter the student's name: ")
grad_year = int(input("Please enter the year that the students will graduate: "))
levels = ["Graduated", "Senior", "Junior", "Sophomore", "Freshman"]
level = levels[grad_year - curr_year]
print(name + " is a " + level)
