#File: Project_7_Fridas_Museum_Advanced_Loops.py
#Author: Albert Schultz
#Date: 05/12/2023
#Descriptions: This is unlike the previous projects since this project was an open-ended project. In this scenario, I have been hired to work on a retrospective of Frida Kahlo’s work at a major museum in Mexico. My job is to put together the audio tour, but in order to do that, I need to create a list of each painting featured in the exhibit, the date it was painted, and its spot on the tour.

#Create a list called, paintings and add the following titles: 'The Two Fridas', 'My Dress Hangs Here', 'Tree of Hope', 'Self Portrait With Monkeys'
paintings = ['The Two Fridas', 'My Dress Hangs Here', 'Tree of Hope', 'Self Portrait With Monkeys']

#Create a second list called, dates and give it the following information: 1939, 1933, 1946, 1940.
dates = [1939, 1933, 1946, 1940]

#Zip the two variable lists, paintings and dates together using the function, zip() and print the results to see it in list form.
paintings = zip(paintings, dates)

#Add the three paintings to the paintings_list: 'The Broken Column', 1944 : The Wounded Deer', 1946 : Me and My Doll', 1937'
paintings = ['The Two Fridas', 'My Dress Hangs Here', 'Tree of Hope', 'Self Portrait With Monkeys']
dates = [1939, 1933, 1946, 1940]

paintings = zip(paintings, dates)

paintings_list = list(paintings)
paintings_list.append(("The Broken Column",1944))
paintings_list.append(("The Wounded Deer",1946))
paintings_list.append(("Me and My Doll",1937))

print(paintings_list)

#Find out how many paintings are in the paintings_list variable.
print(len(list(paintings_list)))

#Use the range method to generate a list of identification starts from 1 and is equal to the length of our paintings_list variable. Print out the audio_tour_number as a list.
audio_tour_number = range(1,len(list(paintings_list)))
print(list(audio_tour_number))

#Now, let's zip the variables, audio_tour_number with paintings and save it as master_list variable.
master_list = zip(audio_tour_number, paintings_list)

#Print the zipped master_list to the console.
print(list(master_list))