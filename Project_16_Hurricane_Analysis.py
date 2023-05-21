#File: Project_16_Hurricane_Analysis.py
#Author: Albert Schultz
#Date: 05/19/2023
#Version: 1.00
#Descriptions: This project script goes through the process of organizing and manipulating raw data about Category 5 Hurricanes. I would have the strongest hurricanes as rated by their wind speed. Each one fo these functios would use a number of parameters, conditionals, lists, dictionaries, string manipulation, and return statements to make sense of the hurricane data.

#Review and create the variables for these hurricane data sets.
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael'] #Names of hurricanes.

months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October'] #Months of hurricanes.

years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018] #Years of the hurricanes.

max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160] #Maximum sustained windws (miles per hour - MPH) of hurricanes.

areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']] #Areas affected by the hurricanes.

damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B'] #Damages (USD($) of hurricanes.

deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74] #Deaths for each hurricanes.

#Create a function that shows the damages across the areas.
def update_damages(damages):
    new_damages = []
    conversion = {"M": 1000000,
                  "B": 1000000000}
    for damage in damages:
        if damage == 'Damages not recorded':
            new_damages.append(damage)
        elif damage[-1] in conversion.keys():
            new_value = float(damage[:-1]) * conversion[damage[-1]]
            new_damages.append(new_value)

    return new_damages

#Print the updated damages here.
updated_damages = update_damages(damages)
print(updated_damages)

#Create an empty hurricane list for now.
hurricanes = {}

#Create a dictionary of hurricanes and associate 6 key data points to the hurricanes below in a function.
def construct_hurricanesionary(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
    for i in range(len(names)):
        hurricanes[names[i]] = {'Name': names[i], 'Month': months[i], 'Year': years[i],
                                'Max Sustained Wind': max_sustained_winds[i], 'Areas Affected': areas_affected[i],
                                'Damage': damages[i], 'Death': deaths[i]}
    return hurricanes

#Print out the entire list of the data point list table.
print(
    construct_hurricanesionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths))
print(hurricanes["Carol"])

#Create a function that would divide the hurricane based on the year.
def hurricane_by_year_dictionary(year):
    hurricane_by_year = []
    for name in hurricanes:
        if hurricanes[name]['Year'] == year:
            hurricane_by_year.append(hurricanes[name])
    return hurricane_by_year

#Print the hurricane by year lookup in the function below.
print(hurricane_by_year_dictionary(2016))
print(hurricane_by_year_dictionary(2017))

areas_affected = {}

#Create a function that determines the numbers of affected areas per hurricane.
def count_affected_areas(dict):
    for name in dict:
        for area in dict[name]['Areas Affected']:
            if area in areas_affected:
                areas_affected[area] += 1
            else:
                areas_affected[area] = 1
    return areas_affected

#Print out the list of affected areas based on hurricanes.
print(count_affected_areas(hurricanes))

#Create a function that goes through the most affected area.
def most_affected_area(dict):
    values = sorted(list(dict.values()), reverse=True)
    for area in dict.keys():
        if values[0] == dict[area]:
            return area, dict[area]

#Print the most affected areas by hurricanes here.
print(most_affected_area(areas_affected))

#Create a function that determines the greatest amount of deaths by hurricanes here.
def greatest_num_deaths(dict):
    max_death = 0
    hurricane_name = ''
    for name in dict:
        if dict[name]['Death'] > max_death:
            max_death = dict[name]['Death']
            hurricane_name = name
    return hurricane_name, max_death

#Print the greatest numbers of death by hurricanes here.
hurricane_mortality = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
print(greatest_num_deaths(hurricanes))

#Write the categorize by mortality here.
def categorize_by_mortality(dict):
    mortality_scale = {0: 0,
                       1: 100,
                       2: 500,
                       3: 1000,
                       4: 10000}
    for name in dict:
        if dict[name]['Death'] == mortality_scale[0]:
            hurricane_mortality[0] = name
        elif mortality_scale[0] < dict[name]['Death'] <= mortality_scale[1]:
            hurricane_mortality[1].append(name)
        elif mortality_scale[1] < dict[name]['Death'] <= mortality_scale[2]:
            hurricane_mortality[2].append(name)
        elif mortality_scale[2] < dict[name]['Death'] <= mortality_scale[3]:
            hurricane_mortality[3].append(name)
        elif mortality_scale[3] < dict[name]['Death'] <= mortality_scale[4]:
            hurricane_mortality[4].append(name)
        else:
            hurricane_mortality[5].append(name)
    return hurricane_mortality

#Print the categorize by mortality rate by hurricane function here.
print(categorize_by_mortality(hurricanes))

#Write the greatest function here.
def greatest_damage_function(dict):
    damages_list = []
    for name in dict:
        if dict[name]['Damage'] != 'Damages not recorded':
            damages_list.append(dict[name]['Damage'])

    greatest_damage = max(damages_list)

    for name in dict:
        if dict[name]['Damage'] == greatest_damage:
            return name, greatest_damage

#Print the greatest damage by hurricanes function here.
print(greatest_damage_function(hurricanes))

damage_scale_hurricane = {'No Damage': [], 1: [], 2: [], 3: [], 4: [], 5: []}

#Write the categorizes by damage function here.
def categorise_by_damage(dict):
    damage_scale = {0: 0,
                    1: 100000000,
                    2: 1000000000,
                    3: 10000000000,
                    4: 50000000000}

    for name in dict:
        if dict[name]['Damage'] == 'Damages not recorded':
            damage_scale_hurricane['No Damage'].append(name)
        elif damage_scale[0] < dict[name]['Damage'] <= damage_scale[1]:
            damage_scale_hurricane[1].append(name)
        elif damage_scale[1] < dict[name]['Damage'] <= damage_scale[2]:
            damage_scale_hurricane[2].append(name)
        elif damage_scale[2] < dict[name]['Damage'] <= damage_scale[3]:
            damage_scale_hurricane[3].append(name)
        elif damage_scale[3] < dict[name]['Damage'] <= damage_scale[4]:
            damage_scale_hurricane[4].append(name)
        else:
            damage_scale_hurricane[5].append(name)
    return damage_scale_hurricane

#Print the categories by damage based on the hurricanes.
print(categorise_by_damage(hurricanes))