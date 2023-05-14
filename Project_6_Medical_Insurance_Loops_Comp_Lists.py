#File: Project_6_Medical_Insurance_Loops_Comp_Lists.py
#Author: Albert Schultz
#Date: 05/11/2023
#Descriptions: In this project script, I went over the estimation of the insurance premium for each person in this sample data set below using Python comprehension lists to loops to make sense of the insurance premiums.

#Create three variable lists with the sample information about the insurance data.
names = ["Judith", "Abel", "Tyson", "Martha", "Beverley", "David", "Anabel"]
estimated_insurance_costs = [1000.00, 2000.00, 3000.00, 4000.00, 5000.00, 6000.0, 7000.00]
actual_insurance_costs = [1100.0, 2200.0, 3300.0, 4400.0, 5500.0, 6600.0, 7700.0]
total_cost = 0

#Create a for loop that iterate through actual_insurance_costs and add each insurance cost to the variable, total_cost.
for insurance_cost in actual_insurance_costs:
  total_cost += insurance_cost

#Create a variable called, average_cost that stores the total_cost/len(actual_insurance_costs).
average_cost = total_cost/len(actual_insurance_costs)

#Print the average cost with the following message.
print(f"The average cost of the actual insurance cost per person is, ${str(average_cost)}.")

#Write a for loop with a variable i that goes from 0 to len(names). Leave it empty for now.
for i in range(len(names)):
  name = names[i]
  insurance_cost = actual_insurance_costs[i]
  print(f"The insurance cost for {name} is ${str(insurance_cost)}.")
  #Create a if condition to check whether the insurance cost is above, below, or equal to the average insurance cost.
  if insurance_cost > average_cost:
    print(f"The insurance cost for {name} is above average.")
  elif insurance_cost < average_cost:
    print(f"The insurance cost for {name} is less than the average.")
  else:
    print(f"The insurance cost for {name} is equal to the insurance average.")

#Create a comprehension list for the variable, updated_estimated_costs.
update_estimated_costs = [estimate_cost*(11/10) for estimate_cost in estimated_insurance_costs]
print(list(update_estimated_costs))