#File: Project_18_Performing_Linear_Regresssion_Scenario.py
#Author: Albert Schultz
#Date: 05/21/2023
#Version: 1.00
#Descriptions: This project goes through the process of identifying the distances between points, the lines, and determining the errors based on the location on the plot of the graph using linear regression.

#Create the formula needed for the script.
#y = m*x+b

#Create the function that would be use to find the y value.
def get_y(m, b, x):
    y = m*x+b
    return y

#Test the formula function below.
print(get_y(1, 0, 7) == 7)
print(get_y(5, 10, 3) == 25)

#Define a funciton that would calculate the error between the lines.
def calculate_error(m, b, point):
    x_point, y_point = point
    y = m*x_point + b
    distance = abs(y - y_point)
    return distance

#Test the functions using the four values below.
print(calculate_error(1, 0, (3,3)))
print(calculate_error(1, 0, (3,4)))
print(calculate_error(1, -1, (3,3)))
print(calculate_error(-1, 1, (3,3)))

#Define the data data matrix below for datapoints.
datapoints = [(1,1),(2,0),(3,4),(4,4),(5,3)]

#Iterate through each point in points and calculate the error from the point to the line using the calculate error function.
def calculate_all_error(m, b, point):
    total_error = 0
    for point in datapoints:
        point_error = calculate_error(m, b, point)
        total_error += point_error
    return total_error

#Every point in the data set lies upon the y=x, so the total erorr should be zero.
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(1, 0, datapoints))

#every point in this dataset is 1 unit away from y = x + 1, so the total error should be 4:
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(1, 1, datapoints))

#every point in this dataset is 1 unit away from y = x - 1, so the total error should be 4:
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(1, -1, datapoints))

#the points in this dataset are 1, 5, 9, and 3 units away from y = -x + 1, respectively, so total error should be
# 1 + 5 + 9 + 3 = 18
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(-1, 1, datapoints))

#Using list comprehension, let's create a list of possible m values to try. Make the list, possible_ms that goes from -10 to 10 inclusive, in increment of 0.1.
possible_ms = [m*0.1 for m in range(-100,101)]

#Make a comprehension list between -200 and 201 between the values of -20 to 20 inclusive.
possible_bs = [b*0.1 for b in range(-200, 201)]

#Create the variables needed to run through the possible ms in the for loop.
datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]
smallest_error = float("inf")
best_m = 0
best_b = 0

for m in possible_ms:
    for b in possible_bs:
        error = calculate_all_error(m, b, datapoints)
        if error < smallest_error:
            best_m = m
            best_b = b
            smallest_error = error

print(best_m, best_b, smallest_error)

#Now, we have the data that needs to use to predict the distance the item would bounce to in terms of distance. Y = 0.3x + 1.7.

#Run the quick test using the above found predicted values.
print(f"The distance for the width of 6 cm ball would bounce a distance to, {str(get_y(0.3, 1.7, 6))} meters.")
