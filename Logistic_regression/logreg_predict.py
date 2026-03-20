import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from helper_functions.min import ft_min
from helper_functions.max import ft_max
from helper_functions.avg import ft_avg
from helper_functions.percentile import ft_percentile
from helper_functions.std import ft_std

import sys
import pandas as pd

def normalize(col):
    col_min = ft_min(col)
    col_max = ft_max(col)
    return [(x - col_min)/ (col_max - col_min) for x in col]

if len(sys.argv) != 2:
    exit(1)

file = pd.read_csv(sys.argv[1], sep=",")

subjects = ['Arithmancy', 'Astronomy', 'Herbology', 'Defense Against the Dark Arts', 
                'Divination', 'Muggle Studies', 'Ancient Runes', 'History of Magic', 
                'Transfiguration', 'Potions', 'Care of Magical Creatures', 'Charms', 'Flying']

col1 = []
col2 = []

#nettoyage des donnees

raw_features = zip(file[subjects[7]], file[subjects[8]])
houses = file['Hogwarts House']
for x, y in raw_features:
    if not pd.isna(x) and not pd.isna(y):
        col1.append(x)
        col2.append(y)

#normalisation des donnees
col1 = normalize(col1)
col2 = normalize(col2)
print(col1)
print(col2)

#labelisation de la data

possible_houses = ["Hufflepuff", "Gryffindor", "Ravenclaw", "Slytherin"]

labeled_houses = {}
for house in possible_houses:
    labeled_houses[house] = 
