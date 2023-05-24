#File: Project_19_Strings_Authors_Extractor_Analysis.py
#Author: Albert Schultz
#Date: 05/23/2023
#Version: 1.00
#Descriptions: This project extracts raw highlighted_poems from the raw data set of authors and the associated authors.

highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

#Review the poem below.
print(highlighted_poems)

#Split the poems based on the comma.
highlighted_poems_list = highlighted_poems.split(',')

#Print the results below.
print(highlighted_poems_list)

#Create empty variables called, highlighted_poems_stripped and highlighted_poems_details.
highlighted_poems_stripped = []
highlighted_poems_details = []
titles = []

#Create a for loop and append the data to the stripped and detailed poems list.
for poem in highlighted_poems_list: #First for loop extract the spaces and append changes to highlighted_poems_stripped list.
    highlighted_poems_stripped.append(poem.strip())

for highlights in highlighted_poems_stripped: #Second for loop that append the highlight details with changes to the stripped list that was appended for the strip() method and further separate the words if they have : beteen them.
    highlighted_poems_details.append(highlights.split(':'))

#Print the data below.
print(highlighted_poems_details)

#Look at the list and extract based on the index from 0 to 2 into title, author, and year variables.
print(type(highlighted_poems_details)) #Id as list type.

#Find the numbers of cells.
print(len(highlighted_poems_details))

#Iter through the list using for loop.
index = 0
while index < len(highlighted_poems_details):
    print(highlighted_poems_details[index])
    index += 1

print('\n') #Insert break.

#Create empty lists for the authors, title, and year.
authors = []
titles = []
years = []

print(highlighted_poems_details[0][0]) #Get test title of book.
print(highlighted_poems_details[0][1]) #Get test author of book.
print(highlighted_poems_details[0][2]) #Get test year of book.

#Create several for loops and append changes to authors, titles, and years for each for loop.
for author in highlighted_poems_details:
    authors.append(highlighted_poems_details[0][1])
print(authors) #Cleaned authors list.

for title in highlighted_poems_details:
    titles.append(highlighted_poems_details[0][0])
print(titles) #Cleaned book titles list.

for year in highlighted_poems_details:
    years.append(highlighted_poems_details[0][2])
print(years) #Cleaned book years list.

#Count the numbers of items in the book titles.
print(f"The total numbers of books are {str(len(titles))}.")
print(f"The total numbers of authors are {str(len(authors))}.")
print(f"The total numbers of years are {str(len(years))}.")