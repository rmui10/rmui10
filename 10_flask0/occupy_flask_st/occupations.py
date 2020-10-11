#Team Asinine - Winnie Huang, Renee Mui, Anya Zorin
#SoftDev
#K10 -- Putting Little Pieces Together: display random job on webpage
#2020-10-11

#based off of Winnie's original homework

import csv
import random

reader = csv.DictReader(open('occupations.csv'))  #allows us to read the csv file
dictionary = {                                    #sets up a destination for the contents of the csv file
    'job occupation': [],
    'percentage': []
}

for row in reader:                                #stores the contents of the csv file into the dictionary by iterating line by line
    dictionary['job occupation'].append(row['Job Class'])      
    dictionary['percentage'].append(float(row['Percentage']))  

dictionary['job occupation'].pop()                #gets rid of the 'Total' entry
dictionary['percentage'].pop()                    #gets rid of the 99.8 entry

dictionary['job occupation'].append('None')       #creates an option for missing percentage
dictionary['percentage'].append(0.2)              #missing percentage out of 100% probability

def getDict(): #allows us to access dictionary from other files
    return dictionary

def getJob(): #returns random weighted occupation
    return random.choices(getDict()['job occupation'], weights=getDict()['percentage'], k=1)[0]

print(getJob())
