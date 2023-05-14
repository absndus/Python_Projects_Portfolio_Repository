#Title: Project_2_Medical_Insurance_Functions.py
#Author: Albert Schultz
#Date: 05/14/2023
#Notes: This python scripts goes through the process of understanding various information such as age, sex, BMI, numbers of children, and smoking status that contributes to medical insurance costs using custom functions.

#Create the initial variables below.
name = input("Enter your first and last name: ")
age = int(input("Enter the age here in years: "))
sex = int(input("Enter 0 for male and 1 for female: "))
bmi = float(input("Enter the BMI here: "))
num_of_children = int(input("Enter the number of children you currently have: "))
smoker = int(input("Enter 0 if you are a non-smoker and 1 if you are a smoker: "))

#Create a new function called, calculate_insurance_cost().
def calculate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
    #Estimate the user's input insurance cost.
    insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
    #Print insurance cost with their input name.
    print(f"The estimated insurance cost for {name} is ${str(insurance_cost)}.")
    return insurance_cost

#Print the user's insurance cost by calling the function, calculate_insurance_cost().
calculate_insurance_cost(name, age, sex, bmi, num_of_children, smoker)