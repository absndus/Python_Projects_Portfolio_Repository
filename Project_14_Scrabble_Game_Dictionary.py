#File: Project_14_Scrabble_Game_Dictionary.py
#Author: Albert Schultz
#Date: 05/16/2023
#Version: 1.00
#Descriptions: This project script goes through the process of utilizing the provided variable lists, letters and points and convert them to dictionary list for further dictionary manipulations.

#Create the variable lists below.
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

#Combine the two above variable lists into a dictionary. Use the zip() method to create a dictionary called, letter_to_points.
letter_to_points = zip(letters, points) #Zip the two variable lists.
print(list(letter_to_points),"\n") #View the list.

letter_to_points_dict = {key:value for key, value in zip(letters, points)} #Converts the two list into one zipped dictionary list.

#list dicitonary list variables below.
print(letter_to_points_dict)

#Add an element to the letter_to_points_dict dictionary.
letter_to_points_dict[""] = 0

#View the modified dictionary.
print(letter_to_points_dict)