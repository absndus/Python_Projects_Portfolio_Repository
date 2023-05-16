#File: Project_11_Magic_8_Ball.py
#Author: Albert Schultz
#Date: 05/16/2023
#Version: 1.00
#Descriptions: This project script goes through the answer using the random number generator that generates different answers when the program is run each time.

#Import library modules.
import random

#Create variables that were needed in the script.
name = input("Enter your first and last name: ")
question = input("Enter a true and false question: ")
answer = ""
random_number = random.randint(1,9)

#Run the print() of the random_number.
#print(random_number)

#Create an elif statement.
if random_number == 1 and name != "":
  answer = "Yes - definetly"
elif random_number == 2 and name != "":
  answer = "It is decidedly so"
elif random_number == 3 and name != "":
  answer = "Without a doubt"
elif random_number == 4 and name != "":
  answer = "Reply hazy, tray again"
elif random_number == 5 and name != "":
  answer = "Ask again later"
elif random_number == 6 and name != "":
  answer = "Better not tell now"
elif random_number == 7 and name != "":
  answer = "My sources say no"
elif random_number == 8 and name != "":
  answer = "Outlook not so good"
elif random_number == 9 and name != "":
  answer = "Very doubtful"
else:
  answer = "Error, enter an answer."

#Print the information below.
print(f"{name} asks: {question}")
print(f"Magic 8-Ball's answer: {answer}")