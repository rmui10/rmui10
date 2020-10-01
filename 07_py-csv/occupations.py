# Triple M: Maddy Andersen, Mary Shang, Renee Mui
# SoftDev
# K07 -- StI/O: Divine your Destiny! - returns a randomly selected occupation based on information from a csv file
# 2020-10-02

'''
To return a randomly selected occupation where the results are weighted based on
the percentages given, we first generated a random number between 0 and 99.8 (which
was the sum of all the percentages). We then looped through each row and subtracted
the percentage at that row from the random number. Once the random number became
negative, we printed out the occupation at that row.

Ex: If the random number was 10.1, we would first subtract 6.1 (percentage for management),
giving us 4.0. Then we subtract 5.0 for business and financial operations, giving us a
negative number. Therefore, the chosen occupation would be business and financial operations.
'''

# imports the csv and random modules needed later on
import csv
import random

# creates a global variable to store the dictionary of occupations
copyDict = {}

# reads in csv file and converts it to a dictionary
with open('occupations.csv', newline = '') as csvfile:
    reader = csv.DictReader(csvfile)

    # changes the percentages from strings to floats
    # and copies each row to copyDict
    for row in reader:
        row['Percentage'] = float(row['Percentage'])
        # print(row['Job Class'], row['Percentage'])
        copyDict[row['Job Class']] = row['Percentage']

# picks a random occupation based on percentages
def pick(d):

    # picks a random number from 0 to 99.8
    r = random.randrange(998) / 10
    # print(r)

    # loops through all the keys and values in the dictionary
    for key, value in d.items():

        # subtracts the percentage at that row from the random number
        r -= value

        # the chosen occupation would be the one when the random number became negative
        if (r < 0):
            return key


print(pick(copyDict))
