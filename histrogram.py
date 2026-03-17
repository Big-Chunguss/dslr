from helper_functions.min import ft_min
from helper_functions.max import ft_max
from helper_functions.avg import ft_avg
from helper_functions.percentile import ft_percentile
from helper_functions.std import ft_std

import matplotlib.pyplot as plt
import numpy as np
import sys
import csv

if len(sys.argv) != 2:
    print("You need a single file path")
    exit(1)
with open(sys.argv[1]) as file:
    csv_reader = csv.DictReader(file, delimiter=",")
    columns = csv_reader.fieldnames

# 1st function: get all house names and subjects
    hogwarts_house = []
    subjects = []
    count = 1
    for row in csv_reader:
        if count:
            for index in row:
                if index not in subjects and index != "Index":
                    try:
                        float(row[index])
                        subjects.append(index)
                    except ValueError:
                        pass
                count = 0
        if row["Hogwarts House"] not in hogwarts_house:
            hogwarts_house.append(row["Hogwarts House"])
    # print(hogwarts_house)
    print(subjects)

    file.seek(0)
    csv_reader = csv.DictReader(file, delimiter=",")
# 2nd function: create datasets for each house
    db_houses = {house: [] for house in hogwarts_house}
    for row in csv_reader:
        if row["Hogwarts House"] in hogwarts_house:
            # print(row)
            db_houses[row["Hogwarts House"]].append(row)
    # print(db_houses["Hufflepuff"])

# 3rd function plot them for each subject

for houses in hogwarts_house:
    print(f"==={houses}===")
    tmp = {classes: [] for classes in subjects}
    min_std = float('inf')
    min_subject = None  
    for classes in subjects:
        for rows in db_houses[houses]:
            try:
                tmp[classes].append(float(rows[classes]))
            except ValueError:
                continue
        std_val = ft_std(tmp[classes])
        if std_val < min_std:
            min_std = std_val
            min_subject = classes
    plt.hist(tmp[min_subject])
    plt.title(f"Score Distribution for '{min_subject}' by {houses}")
    plt.xlabel("Score")
    plt.ylabel("Number of Students")
    plt.show()
    print(f"Subject with lowest standard deviation for {houses}: {min_subject} ({min_std})")