"""
    Author: LemanSachs29
    Date: 06/11/2025
    Description: Create a program that ask the user for a date and reports whether it is valid
    Note: In this program the date format is DD/MM/YYYY
"""

day = int()
month = int()
year = int()

# Ask to the user by the day
print("Day (1 - 31): ", end=" ")
day = int(input())
while day < 1 or day > 31:
    print("Day (1 - 31): ", end=" ")
    day = int(input())

# Ask to the user by the month
print("Month (1 - 12): ", end=" ")
month = int(input())
while month < 1 or month > 12:
    print("Month (1 - 12): ", end=" ")
    month = int(input())

# Ask to the user by the year
print("Year ( >= 0): ", end=" ")
year = int(input())
while year <= 0:
    print("Year (1 - 31): ", end=" ")
    year = int(input())

# A date is invalid if any of the following holds:
# 1) Day = 31 for months that have only 30 days (Apr, Jun, Sep, Nov).
# 2) Day = 30 in February.
# 3) Day = 29 in February of a non-leap year.

if ((day == 31 and (month != 4 and month != 6 and month != 9 and month != 11)) 
    or (day == 30 and month == 2) 
    or day == 29 and month == 2 and not ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0))):
    msg = " incorrect."
else:
    msg = " correct. "

# Printing the answer
print("The date " + str(day) + "/" + str(month) + "/" + str(year) + " is " + msg)



