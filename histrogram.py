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
    print(hogwarts_house)
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
std_dev = []

for classes in subjects:
    print(f"==={classes}===")
    tmp = {house: [] for house in hogwarts_house}
    for houses in hogwarts_house:
        for rows in db_houses[houses]:
            try:
                tmp[houses].append(float(rows[classes]))
            except ValueError:
                continue
        print(houses)
        print(ft_std(tmp[houses]))

for houses in hogwarts_house:
    print(f"==={houses}===")
    tmp = {classes: [] for classes in subjects}
    min = []
    for classes in subjects:
        for rows in db_houses[houses]:
            try:
                tmp[classes].append(float(rows[classes]))
            except ValueError:
                continue
        print(classes)
        min.append(ft_std(tmp[classes]))
        print(ft_std(tmp[classes]))
    print(ft_min(min))

# plt.hist(hufflepuff)

#     float_columns = []
#     for col in columns:
#         if col.lower() == "index":
#             continue
#         try:
#             all_floats = any(float(row[col]) if row[col] else False for row in csv_reader)
#             if all_floats:
#                 float_columns.append(col)
#         except ValueError:
#             continue

#     file.seek(0)
#     csv_reader = csv.DictReader(file, delimiter=",")

#     column_values = {col: [] for col in float_columns}
#     mean = 0
#     for row in csv_reader:
#         mean += 1
#         for col in float_columns:
#             value = row.get(col)
#             if value:
#                 try:
#                     column_values[col].append(float(value))
#                 except ValueError:
#                     print(f"Skipping invalid value in column {col}: {value}")




x = np.random.normal(170, 10, 250)

plt.hist(x)
plt.show()
plt.savefig('histogram.png')
print("Histogram saved to histogram.png") 