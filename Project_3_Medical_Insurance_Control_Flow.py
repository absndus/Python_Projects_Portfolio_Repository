#File: Project_3_Medical_Insurance_Control_Flow.py
#Author: Albert Schultz
#Date: 05/09/2023
#Descriptions: In this project, I examined how factors such as age, sex, number of children, and smoking status contribute to medical insurance costs. I have applied my knowledge of Python control flow to write the codes that gives people advice on how to lower their medical insurance costs.

#Create input variables for the program to take the data into the function, estimate_insurance_cost() into an account to generate the printed amount of estimated premiums.
name = input("Enter your first and last name: ")
age = int(input("Enter your age in years: "))
sex = int(input("Enter 0 for female and 1 for male: "))
num_of_children = int(input("Enter the number of children: "))
smoker = int(input("Enter 0 for non-smoker and 1 for smoker: "))

#Formula for Insurance cost for an individual: Ic = 400 x age - 128 x sex + 425 x Childrenn + 10000 x Smoker - 2500

#Create a insurance_cost function with an if-else statement.
def estimate_insurance_cost(name, age, sex, num_of_children, smoker):
    estimated_cost = 400*age - 128*sex + 425*num_of_children + 10000*smoker - 2500
    print(f"{name}'s Estimated Insurance Cost: ${str(estimated_cost)}.")
    if smoker == 1:
        print("To lower your cost, you should consider quitting smoking.")
    else:
        print("Smoking is not an issue for you.")
    return estimated_cost

#Call the estimate_insurance_cost() function.
estimate_insurance_cost(name, age, sex, num_of_children, smoker)