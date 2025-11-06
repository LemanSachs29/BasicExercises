import math

"""
    Author: LemanSachs29
    Date: 04/11/2025
    Description: Create a program what ask the user for a number and a position.
        then the program will display the digit in that position.
"""

number = int()
tmp = int()
position = int()
numberOfDigits = 1
obtainedDigit = int()


print("Enter a positive number: ", end = " ")
number = int(input())
while number <= 0:
    print("Enter a positive number: ", end = " ")
    number = int(input())


tmp = number
while tmp // 10 != 0:
    numberOfDigits += 1
    tmp = tmp // 10
    

print("Enter a position between 1 and " + str(numberOfDigits), end = " ")
position = int(input())
while (position < 1 or position > numberOfDigits):
    print("Enter a position between 1 and " + str(numberOfDigits), end = " ")
    position = int(input())


obtainedDigit = (number // int(pow(10, numberOfDigits - position))) % 10

print("The digit in position " + str(position) + " is " + str(obtainedDigit))
