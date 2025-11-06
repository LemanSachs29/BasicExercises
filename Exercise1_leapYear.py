"""
    Author: LemanSachs29
    Date: 06/11/2025
    Description: Create a program what ask the user for a year. 
        then the program will display if the year is leap.
"""

year = int()
msg = str()

print("Year: ", end = " ")
year = int(input())
while year <=0:
    print("Year: ", end = " ")
    year = int(input())


if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    msg = " is a "
else:
    msg = " is not a "

print("Year " + str(year) +  msg + "leap year")