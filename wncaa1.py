'''
Women's 2025 NCAA Swimming Psych Sheets
Author: Orly Olbum
Start Date: April 2, 2025
Goal: Initial EDA for 2025 ncaa swimming psych sheets
'''

# libraries
import pandas as pd

# data load
wncaa = pd.read_csv('ncaa25_psychsheets.csv')
# print(wncaa.columns)
# we have first and last name, let's make one more field for both so we can count the swimmers
wncaa['Full Name'] = wncaa['First'] + ' ' + wncaa['Last']
# print(wncaa.head())

'''
intro stats!
what is up with this dataset!
i love swimming!

level 1: easy summaries, easy questions
'''

# how many swimmers were there
swimmers = wncaa['Full Name'].unique()
# print(len(swimmers))

# how many schools were represented
teams = wncaa['Team'].unique()
# print(len(teams))

# top 5 schools by number of swimmers


# 


# top 5 swimmers buy number of events




'''
level 2: cross-sections of the data needed to answer slightly more complicated questions
'''




'''
level 3: EARTH-SHATTERING STATS

jk but some more complicated wizardry will be required to answer these ones
'''