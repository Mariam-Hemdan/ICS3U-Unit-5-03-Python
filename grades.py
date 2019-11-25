#!/usr/bin/env python3

# Created by : Mariam Hemdan
# Created on : November 2019
# This function takes the level to grade and returns the middle percentage mark


def calculate_mark(grade):
    # calculate percentage mark
    return_value = None

    # process
    if grade == "4+":
        return_value = 97
    elif grade == "4":
        return_value = 90.5
    elif grade == "4-":
        return_value = 83
    elif grade == "3+":
        return_value = 78
    elif grade == "3":
        return_value = 74.5
    elif grade == "3-":
        return_value = 71
    elif grade == "2+":
        return_value = 68
    elif grade == "2":
        return_value = 64.5
    elif grade == "2-":
        return_value = 61
    elif grade == "1+":
        return_value = 58
    elif grade == "1":
        return_value = 54.5
    elif grade == "1-":
        return_value = 51
    elif grade == "R":
        return_value = 45
    elif grade == "NE":
        return_value = 35

    return return_value


def main():
    # this function gets the grade

    # input
    grade = (input("Enter the grade:"))
    print("")

    # call functions
    level = calculate_mark(grade)
    print(level)


if __name__ == "__main__":
    main()
