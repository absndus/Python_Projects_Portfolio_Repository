#File: Project_17_Medical_Insurance_Python_Dictionaries.py
#Author: Albert Schultz
#Date: 05/21/2023
#Version: 1.00
#Descriptions: This project goes through the setup of the US Medical Insurance script by utilizing Python Dictionaries to manage data and present the information to the console.

#Create list variables of sample Medical Insurances.
medical_costs = {} #Empty medical costs dictionary

#Add data to the medical_costs dictionary by adding Marina and Vinay.
medical_costs['Marina'] = 6607.0
medical_costs['Vinay'] = 3225.0

#Print the new appended records of the medical costs dictionary below.
print(medical_costs)

#One a single line of code, update the medical records dictionary with three people; Connie, Isaac, and Valentina. To update, use the update({}) bracket methods to properly add records to the existing data set.
medical_costs.update({'Connie':8886.0,'Isaac':16444.0,'Valentina':6420.0})

#Print out the updated version of the medical records dictionary below.
print(medical_costs)

#The insurance cost of Vinay's record was incorrect. Change the cost from 3225.0 to 3325.0.
medical_costs.update({'Vinay':3325.0})
#Print the up to date corrected medical costs dictionary below.
print(medical_costs)

#Create a variable called, total_cost and set it to 0.
total_cost = 0
sum_records = 0

#Iterate through the values in medical_costs and add each value to tthe total_cost variable.
for cost in medical_costs.values():
    total_cost += cost

#Iterate through the medical costs dictionary to count how many records are in the set.
sum_records = len(medical_costs.keys())

#Only allow two decimal place and name it, cost_decimal.
cost_decimal = "{:.2f}".format(total_cost)

#After the loop, create a variable called, average_cost that stores cost_decimal / len(medical_costs) dict.
average_cost = "{:.2f}".format(float(cost_decimal)/float(sum_records))

#First, create two lists called names and ages with the following table.
names = ["Marina", "Vinay", "Connie", "Isaac", "Valentina"]
ages = [27, 24, 43, 35, 52]

#Create a zipped variabled called, zipped_ages that is zipped list of pairs between names and ages list.
zipped_ages = zip(names, ages)
print(list(zipped_ages))

#Create a dicitonary called, names_to_ages by using the list comprehension that iterates through zipped ages and turns each pair into a key : value item.
names_to_ages = {names:ages for names, ages in zipped_ages}
print(names_to_ages)

#test_one_dict = {key:value for key, value in zipped_test_dict}
#print(test_one_dict)

#Use the .get() to get value of Marina's age and store it in the variable called, Marina_age. Use none as a default value if key do not exist.
marina_age = names_to_ages.get("Marina", 27)

#Create a third dictionary that represents a database of medical records that contains the patient's name, age, sex, gender, BMI, number of children, smoker status, and insurance cost.
medical_records = {}

#Add Marina to medical records as a key with the value being the medical data.
medical_records['Marina'] = {'Age':27, 'Sex':'Female','BMI':31.1,'Children':2,'Smoker':'Non-smoker','Insurance_cost':6607.0}
print(medical_records)

medical_records['Vinay'] = {'Age':24, 'Sex':'Male','BMI':26.9,'Children':0,'Smoker':'Non-smoker','Insurance_cost':3225.0}
print(medical_records)

medical_records['Connie'] = {'Age':43, 'Sex':'Female','BMI':25.3,'Children':3,'Smoker':'Non-smoker','Insurance_cost':8886.0}
print(medical_records)

medical_records['Isaac'] = {'Age':35, 'Sex':'Male','BMI':20.6,'Children':4,'Smoker':'Smoker','Insurance_cost':16444.0}
print(medical_records)

medical_records['Valentina'] = {'Age':52, 'Sex':'Female','BMI':18.7,'Children':1,'Smoker':'Non-smoker','Insurance_cost':6420.0}
print(medical_records)

#Vinnay moved to a new country and we no longer want to include him in the medical records.
medical_records.pop('Vinay')
print(medical_records)

#Use the for loop to iterate through the items of medical records. For each key value pair, print out the string that has the following.
for name, record in medical_records.items():
    print(f"{name} is a {str(record['Age'])} years old {record['Sex']} who is a {record['Smoker']} with a BMI of {record['BMI']} and the insurance cost is, ${str(record['Insurance_cost'])}.")

#Print the total cost below.
print(f"The total cost of all the Medical Insurances is, ${cost_decimal}.")
print(f"The total records in the Medical Insurance data set is, {sum_records}.")
print(f"The average cost of insurance is, ${average_cost}.")
print(f"The age of Marina is, {marina_age} years old.")
print(f"Connie's medical insuranct cost is, ${medical_records['Connie']['Insurance_cost']}.")