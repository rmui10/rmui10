# Triple M: Renee Mui, Maddy Andersen, Mary Shang 
# SoftDev
# K06 -- Learnination Through Amalgamation: Re-factoring our K05 code with our new teammates 
# 2020-10-01

# imports random module (necessary to use random.choice() later in the code)
import random 

KREWES = {
    'orpheus': ['ERIC', 'SAUVE', 'JONATHAN', 'PAK', 'LIAM', 'WINNIE', 'KELLY', 'JEFFREY', 'KARL', 'ISHITA', 'VICTORIA', 'BENJAMIN', 'ARIB', 'AMELIA', 'CONSTANCE', 'IAN'],
    'rex': ['ANYA', 'DUB-Y', 'JESSICA', 'ALVIN', 'HELENA', 'MICHELLE', 'SHENKER', 'ARI', 'STELLA', 'RENEE', 'MADELYN', 'MAC', 'RYAN', 'DRAGOS'],
    'endymion': ['JASON', 'DEAN', 'MADDY', 'SAQIF', 'CINDY', 'YI LING', 'RUOSHUI', 'FB', 'MATTHEW', 'MAY', 'ERIN', 'MEIRU']
}

# asks user for team name and converts it to all lower case
team = input("Pick a team from orpheus, rex, or endymion: ").lower()

# if the user inputs a name that doesn't match the team name, prompts user to enter a correct team name
while team not in KREWES:
    team = input("Please enter either orpheus, rex, or endymion: ").lower()

# prints a random student name from the chosen team
# uses random.choice()
print(random.choice(KREWES[team]))
