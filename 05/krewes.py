# Team SHWORM (Stella Oh, Helenda Williams, Renee Mui)
# SoftDev
# K05 -- Teamwork, but Better This Time
# 2020-09-26

# A program that will print the name of a randomly-selected student
# from team (orpheus, rex, or endymion)

import random

# Dictionary of team (str) and names in each team (list)
KREWES = {
    'orpheus': ['ERIC', 'SAUVE', 'JONATHAN', 'PAK', 'LIAM', 'WINNIE', 'KELLY', 'JEFFREY', 'KARL', 'ISHITA', 'VICTORIA', 'BENJAMIN', 'ARIB', 'AMELIA', 'CONSTANCE', 'IAN'],
    'rex': ['ANYA', 'DUB-Y', 'JESSICA', 'ALVIN', 'HELENA', 'MICHELLE', 'SHENKER', 'ARI', 'STELLA', 'RENEE', 'MADELYN', 'MAC', 'RYAN', 'DRAGOS'],
    'endymion': ['JASON', 'DEAN', 'MADDY', 'SAQIF', 'CINDY', 'YI LING', 'RUOSHUI', 'FB', 'MATTHEW', 'MAY', 'ERIN', 'MEIRU']
}

# Prints the name of a randomly-selected student from team (orpheus, rex, or endymion)
def pick_name(dictionary):
    # picks random team then a random name from that chosen team
    print(random.choice(random.choice(list(dictionary.values()))))

#test-run of random name
pick_name(KREWES)
