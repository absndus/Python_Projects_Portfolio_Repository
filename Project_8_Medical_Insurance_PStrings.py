#File: Project_8_Medical_Insurance_PStrings.py
#Author: Albert Schultz
#Date: 05/15/2023
#Version: 1.00
#Descriptions: This project script goes through the creation of the Medical Inusrance cost estimator using Python Strings and manipulations of data to make the information presentable to users.
import string
from statistics import mean

#Create required variables needed for this script to run.
medical_data = \
"""Marina Allison   ,27   ,   31.1 , 
#7010.0   ;Markus Valdez   ,   30, 
22.4,   #4050.0 ;Connie Ballard ,43 
,   25.3 , #12060.0 ;Darnell Weber   
,   35   , 20.6   , #7500.0;
Sylvie Charles   ,22, 22.1 
,#3022.0   ;   Vinay Padilla,24,   
26.9 ,#4620.0 ;Meredith Santiago, 51   , 
29.3 ,#16330.0;   Andre Mccarty, 
19,22.7 , #2900.0 ; 
Lorena Hodson ,65, 33.1 , #19370.0; 
Isaac Vu ,34, 24.8,   #7045.0"""

#Calculate the number of medical records in our data.
num_records = 0

#Replace the # with $ in the medical_data variable.
updated_medical_data = medical_data.replace('#', '$')

#Create a for-loop that iterates through the updated_medical_data variable. Add 1 to the num_records when the current character is equal to $.
for character in updated_medical_data:
  if character == "$":
    num_records +=1

#Split the updated_medical_data variable based on the ; in the string.
medical_data_split = updated_medical_data.split(";")

#Create an empty list called, medical_records.
medical_records = []

#Iterate using the for loop and if statements for each medical record. Split the string after each comma and append split string to medical records.
for record in medical_data_split:
  medical_records.append(record.split(','))

#The medical_records is not properly formatted for ease of readability. Create an empty variable called, medical_records_clean.
medical_records_clean = []

#Create a for-loop that iterates through the medical records.
for record in medical_records:
  record_clean = []
  #Nested loop goes through each item in each medical record.
  for item in record:
    #Clean the name space for each record using the item.strip() method.
    record_clean.append(item.strip())
  #Add the cleaned medical record to the medical_record_clean variable list.
  medical_records_clean.append(record_clean)

#Print out the names of each of the ten individuals using the for-loop.
for record in medical_records_clean:
  record[0] = record[0].upper()
  print(record[0])

#Create four empty lists.
names = []
ages = []
bmis = []
insurance_costs = []

#iterate through the medical_records_clean and for each record.
for record in medical_records_clean:
    names.append(record[0])
    ages.append(record[1])
    bmis.append(record[2])
    insurance_costs.append(record[3])

#Create a variable.
total_bmi = 0

#Create a for-loop that iterates through the bmis variable and tally the total using sum.
for bmi in bmis:
    total_bmi += float(bmi)

#Find the mean of the total_bmi.
average_bmi = total_bmi/len(bmis)

#Print out following info to screen.
print("Here is the raw data: \n" + medical_data + "\n")
print("Replaced the # with the % symbole in the medical_data variable: \n" + updated_medical_data + "\n")
print(f"The numbers of records in the updated_medical_records variable is, {num_records} medical records.\n")
print(f"Here is the tabulated split of the updated_medical_data variable: {medical_data_split} \n")
print(f"Here is the tabulated split of the medical_records variable: {medical_records}\n")
print(f"Here is the cleaned medical records data: {medical_records_clean}")
print(f"The names on the record is, {names}")
print(f"The ages on the record is, {ages}")
print(f"The BMIs on the record is, {bmis}")
print(f"The insurance cost for each record is, {insurance_costs} \n")
print(f"Total BMI for the medical records is, {total_bmi}.")
print(f"The average BMI for the medical records is, {average_bmi}")