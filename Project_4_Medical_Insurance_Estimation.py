#File: Project_4_Medical_Insurance_Estimation.py
#Author: Albert Schultz
#Date: 05/09/2023
#Descriptions: In this project, I examined how factors such as age, sex, number of children, and smoking status contribute to medical insurance costs. I have applied my knowledge of Python lists and wrote the code that gives people the insurance premiums.

#Formula for Insurance cost for an individual: Ic = 400 x age - 128 x sex + 425 x Childrenn + 10000 x Smoker - 2500

# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print(name + "'s Estimated Insurance Cost: $" + str(estimated_cost) + ".")
  return estimated_cost

# Estimate Maria's insurance cost
maria_insurance_cost = estimate_insurance_cost(name = "Maria", age = 31, sex = 0, bmi = 23.1, num_of_children = 1, smoker = 0)

# Estimate Rohan's insurance cost
rohan_insurance_cost = estimate_insurance_cost(name =
"Rohan", age = 25, sex = 1, bmi = 28.5, num_of_children = 3, smoker = 0)

# Estimate Valentina's insurance cost
valentina_insurance_cost = estimate_insurance_cost(name = "Valentina", age = 53, sex = 0, bmi = 31.4, num_of_children = 0, smoker = 1)

#Create a new variable called, names.
names = ["Maria", "Rohan", "Valentina"]

#Create a list called, insurance_costs.
insurance_costs = [4150.0, 5320.0, 35210.0]

#Create a new variable, insurance_data that combines names and insurance_costs using zip().
insurance_data = zip(names, insurance_costs)
print(insurance_data)

#Make it readable as a list.
insurance_data = list(insurance_data)
print(insurance_data)

#Create an empty list called, estimated_insurance_data.
estimated_insurance_data = []

#Add Maria's insurance information.
estimated_insurance_data.append(("Maria", maria_insurance_cost))
estimated_insurance_data.append(("Rohan", rohan_insurance_cost))
estimated_insurance_data.append(("Valentina", valentina_insurance_cost))

#Print the combined estimated insurance data for three people.
print(estimated_insurance_data)

#Print the statement for insurance_data should look like.
print(f"Here is the actual insurance cost data: ${str(insurance_data)}.")

#Print the statement for the estimated insurance cost.
print(f"Here is the estimated insurance cost data: ${str(estimated_insurance_data)}.")