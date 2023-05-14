#Title: Project_1_Medical_Insurance.py
#Author: Albert Schultz
#Date: 05/12/2023
#Notes: This Python scripts goes through the process of creating a small program that would provide insights of the medical insurance premiums.

#Create the initial variables below
name = input("Enter your first and last name: ")
age = int(input("Enter your age here: "))
smoker = int(input("Enter if you are a smoker 1 or a non-smoker 0: "))
sex = int(input("Enter if you are a male 0 or a female 1: "))
bmi = float(input("Enter your BMI here in decimal: "))
num_of_children = int(input("Enter the number of children you have: "))

#Add insurance estimate formula below
insurance_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500

print(f"Good day {name}, your insurance cost is ${str(float(insurance_cost))}.")

#Age Factor
age += 4
new_insurance_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print(f"The change in cost of insurance after increasing the age by 4 years is ${change_in_insurance_cost}.")

#BMI Factor
age = 28
bmi += 3.1

new_insurance_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost
print(f"The change is estimated insurance ost after increasing BMI by 3.1 is ${change_in_insurance_cost}.")

#Male vs. Female Factor
sex = 1
bmi = 26.2

new_insurance_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost

print(f"The change in estimated cost for being male instead of female is ${change_in_insurance_cost}.")

#Extra Practice
num_of_children += 2
smoker = 1

new_insurance_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print(f"The change in insurance ost for {name} is, ${change_in_insurance_cost}.")