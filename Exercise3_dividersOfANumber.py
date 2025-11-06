"""
    Author: LemanSachs29
    Date: 06/11/2025
    Description: Create a program what ask the user for a number show all his dividers.
"""


#Ask to the user for a positive number
print("Enter a positive number: ", end = " ")
number = int(input())

# Value de special cases like 0
if number == 0:
    print("Zero does not have dividers")
else:

    #1 Always will be a divider
    print("1, ", end=" ")

    # Look for the rest of dividers until arrive to the half of the number
    for x in range(2, (number//2) + 1):
        if number%x==0:
            print(str(x) + ", ", end=" ")

    #The given number always will be a divider
    print(str(number))

            


