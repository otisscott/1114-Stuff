# Otis Scott
# CS - UY 1114
# 13 Nov 2018
# Homework 8

import csv
import math


def read_file(filename):
    """"
    sig: str -> list(list(str))
    Loads the named file and returns all data rows in the file as
    a list of lists of strings
    """
    with open(filename, 'r') as input_csv:
        reader = csv.reader(input_csv)
        reader.__next__()
        final_list = []
        for row in reader:
            final_list.append(row)
    return final_list


def find_most_exclusive_womens_college(colleges):
    """
    sig: list(list(str)) -> str
    Returns the name of the women's college with the lowest
    admission rate
    """
    top_college = colleges[1]
    for college in colleges:
        if college[22].isdigit() and int(college[22]) == 1:
            if 0 < float(college[24]) < float(top_college[24]):
                top_college = college
    return top_college[3]


def average_sat_score_in_ny(colleges):
    """
    sig: list(list(str)) -> float
    Returns the value of the average SAT score of all
    colleges in New York
    """
    sum_scores = 0
    counter = 0
    for college in colleges:
        if college[5] == 'NY' and college[25] != "NULL":
            sum_scores += int(college[25])
            counter += 1
    return sum_scores / counter


def distance(first , second):
    """
    sig: tuple(float , float), tuple(float , float) -> float
    Returns the Cartesian distance between two points , expressed
    as a latitude/longitude pair
    """
    return math.sqrt(((first[0] - second[0]) ** 2) + ((first[1] - second[1]) ** 2))


def find_college_nearest_center_of_us(colleges):
    """
    sig: list(list(str)) -> str
    Returns the name of the college nearest the
    geographical center of the contiguous United
    States
    """
    closest = colleges[0]
    center = (39.833333, -98.583333)
    for college in colleges:
        if college[18] != "NULL" and college[19] != "NULL":
            if distance((float(college[18]), float(college[19])), center) < distance((float(closest[18]), float(closest[19])), center):
                closest = college
    return closest[3]


def main():
    """
    sig: None -> None
    Prints results from other functions defined above
    """
    colleges = read_file("colleges.csv")
    print("Most exclusive women's college: ", find_most_exclusive_womens_college(colleges))
    print("Average SAT of all NY schools: ", average_sat_score_in_ny(colleges))
    print("College nearest to the geographical center of the contiguous US: ", find_college_nearest_center_of_us(colleges))


main()
