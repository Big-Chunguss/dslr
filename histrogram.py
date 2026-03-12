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

# 1st function: get all house names
    # hogwarts_house = ["Ravenclaw", "Slytherin", "Hufflepuff", "Gryffindor"]
    hogwarts_house = []
    for row in csv_reader:
        for key in row:
            print(key)
            break

# 2nd function: create datasets for each house
# 3rd function plot them for each subject
    float_columns = []
    for col in columns:
        if col.lower() == "index":
            continue
        try:
            all_floats = any(float(row[col]) if row[col] else False for row in csv_reader)
            if all_floats:
                float_columns.append(col)
        except ValueError:
            continue

    file.seek(0)
    csv_reader = csv.DictReader(file, delimiter=",")

    column_values = {col: [] for col in float_columns}
    mean = 0
    for row in csv_reader:
        mean += 1
        for col in float_columns:
            value = row.get(col)
            if value:
                try:
                    column_values[col].append(float(value))
                except ValueError:
                    print(f"Skipping invalid value in column {col}: {value}")




x = np.random.normal(170, 10, 250)

plt.hist(x)
plt.show()
plt.savefig('histogram.png')
print("Histogram saved to histogram.png") 