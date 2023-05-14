#File: Project_5_Medical_Insurance_Advanced_List.py
#Author: Albert Schultz
#Date: 05/09/2023
#Descriptions: In this project, I examined how factors such as age, sex, number of children, and smoking status contribute to medical insurance costs. I have applied my knowledge of simple to advance Python Lists and manipulations of lists into the small insurance estimator.

#Create two variable lists, names and insurance_costs.
names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]

#Append the new individual, "Priscilla" to the names variable. Also, append her insurance cost, 8320.0 to the insurance_costs variable.
names.append("Priscilla")
print(names)

insurance_costs.append(8320.0)
print(insurance_costs)
#By default, it enteres the data at the end of the lists.

#Create anew variable called, medical_records that combines insurance_costs and names into a list using the zip() function.
medical_records = list(zip(insurance_costs, names))
print(medical_records)

#Explore the medical records by storing the length len() of the items in the medical records.
num_medical_records = len(medical_records)
print(f"There are {str(num_medical_records)} medical records.")

#Select the first medical record in medical records variable and save it in first_medical_record.
first_medical_record = medical_records[0]
print(f"Here is the first medical record: {first_medical_record}.")

#Sort medical_records so that the individuals with the lowest insurance costs appears at the start of the list. Then, print and sorted medical_records with the following message.
medical_records.sort()
print(f"Here are the medical records sorted by insurance cost: ${str(medical_records)}")

#Store the cheapest insurance costs in the variable, cheapest_three.
cheapest_three = medical_records[:3]
print(f"Here are the three cheapest insurance costs in our medical records: {str(cheapest_three)}")

#Since the medical_records list and store the three most expensive insurance costs in a list called, priciest_three.
priciest_three = medical_records[-3:]
print(f"Here are the three most expensive insurance costs in our medical records: {priciest_three}.")

#Count the number of occurances of Paul in the names list and store the result in the variable called occurance_paul variable. Print the occurences_paul with the message.
occurences_paul = names.count("Paul")
print(f"There are {str(occurences_paul)} individuals with the name Paul in our medical records.")