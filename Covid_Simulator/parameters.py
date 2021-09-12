# Tells what what the demographics for the population in the simulation
# Demographics.csv will be provided by the researchers

import csv
##########################################################################
# declaring variables////variables waiting to be read from the Demographics file
Title = 0
Population = 0
Pre_existing_conditions = 0
one_ten = 0
eleven_twenty = 0
twentyone_thirty = 0
thirtyone_forty = 0
fortyone_fifty = 0
fiftyone_sixty = 0
sixtyone_seventy = 0
seventyone_eighty = 0
eightyone_ninety = 0
ninetyone_hundred = 0


# prints out variables:

# print(
# Title,
# Population,
# Pre_existing_conditions,
# one_ten ,
# eleven_twenty,
# twentyone_thirty,
# thirtyone_forty,
# fortyone_fifty,
# fiftyone_sixty,
# sixtyone_seventy,
# seventyone_eighty,
# eightyone_ninety,
# ninetyone_hundred
# )
##########################################################################


# opens file, looks for RELATIVE path, r means read, and rename what you will refer to this as
with open('Covid_Simulator/parameters.csv', 'r+') as csv_file:

    # creating variable reader and it will read the given file above, uses DictReader to say what each object is
    csv_reader = csv.DictReader(csv_file)
    # creating variable reader and it will read the given file above, uses Dictreader to say what each object is

    # Column titles:
    # Title,Population,Pre_existing_conditions,1-10,11-20,21-30,31-40,41-50,51-60,61-70,71-80,81-90,91-100


# loops through file to read test
    for line in csv_reader:
        Title = line["Title"]
        Population = int(line["Population"])
        Pre_existing_conditions = float(line["Pre_existing_conditions"])
        one_ten = float(line["1-10"])
        eleven_twenty = float(line["11-20"])
        twentyone_thirty = float(line["21-30"])
        thirtyone_forty = float(line["31-40"])
        fortyone_fifty = float(line["41-50"])
        fiftyone_sixty = float(line["51-60"])
        sixtyone_seventy = float(line["61-70"])
        seventyone_eighty = float(line["71-80"])
        eightyone_ninety = float(line["81-90"])
        ninetyone_hundred = float(line["91-100"])

##########################################################################


# prints out all variables in an easly digestable way:

# print(
# "\nAfter reading file:\n\nTitle: {}\nPopulation: {}\nPre-existing Condition: {}%\n1-10: {}%\n11-20: {}%\n21-30: {}%\n31-40: {}%\n41-50: {}%\n51-60: {}%\n61-70: {}%\n71-80: {}%\n81-90: {}%\n91-100: {}%\n "
# .format(
# Title,
# Population,
# int(Pre_existing_conditions*100),
# int(one_ten*100),
# int(eleven_twenty*100),
# int(twentyone_thirty*100),
# int(thirtyone_forty*100),
# int(fortyone_fifty*100),
# int(fiftyone_sixty*100),
# int(sixtyone_seventy*100),
# int(seventyone_eighty*100),
# int(eightyone_ninety*100),
# int(ninetyone_hundred*100))
# )
