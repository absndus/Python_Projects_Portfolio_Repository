#File: Project_15_Recovery_Comp_Peeps.py
#Author: Albert Schultz
#Date: 05/16/2023
#Version: 1.00
#Descriptions: This project script goes through the steps of managing comp_user csv list and write various json files to the manager about the security issue.

#Import library modules for script.
import csv
import json

#Create a list of users whose creds have been comped, create a new list and save it as, comp_users.
comp_users = []

#Open the creds.csv.
with open('creds.csv') as creds_file:
  creds_csv = csv.DictReader(creds_file)
  for creds_row in creds_csv:
    comp_users.append(creds_row['Username'])

#Start a new file called, comp_user.
with open('comp_user','w') as comp_user_file:
  for comp_user in comp_users:
    comp_user_file.write(comp_user)

#Create a JSON file by converting the above files into the JSON files.
with open('boss_message.json','w') as boss_message:
  boss_message_dict = {
    'recipient':'The Boss',
    'message':'Mission Success'
  }
  #Write out the boss_message_dict to boss_message using json.dump().
  json.dump(boss_message_dict, boss_message)

#Generate new password.csv.
with open('new_creds.csv','w') as new_creds_obj:
  slash_null_sig = """
 _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
"""
  new_creds_obj.write(slash_null_sig)