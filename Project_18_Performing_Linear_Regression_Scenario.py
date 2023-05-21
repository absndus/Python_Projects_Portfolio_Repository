#File: Project_18_Performing_linear_Regression_Scenario.py
#Author: Albert Schultz
#Date: 05/21/2023
#Version: 1.00
#Descriptions: This Python project goes over of utilizing linear regression to understand which line best fits with the least error.
import point as point

#Create input variables.
m = float(input("Enter the number for the variable, m:"))
b = float(input("Enter the number for the variable, b:"))
x = float(input("Enter the number for the variable, x:"))
point = 0

#Write the get_y() function that prints out the answer to y when the user inputs the numbers in the function.
def get_y(m, b, x):
    point = m*x+b
    print(f"The number for y is, {str(point)}.")
    return point

#Check the function above works perfectly.
print(get_y(1,0,7) == 7)
print(get_y(5,10,3) == 25)

#Define the calculate_error() here.
def calculate_error(m,b, point):
    x, y = point
    return abs(y - (m*x+b))
print(f"The test result for m = 1, b = 0, and point(3,3) should be 0, the generated answer was {calculate_error(1,0,(3,3))}.")

print(f"The test result for m = 1, b = 0, and point(3,4) should be 1, the generated answer was {calculate_error(1,0,(3,4))}.")

print(f"The test result for m = 1, b = -1, and point(3,3) should be 1, the generated answer was {calculate_error(1,-1,(3,3))}.")

print(f"The test result for m = -1, b = 1, and point(3,3) should be 5, the generated answer was {calculate_error(-1,1,(3,3))}.")

