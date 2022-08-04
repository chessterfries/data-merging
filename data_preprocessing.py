import csv
import pandas as pd

df = pd.read_csv("dwarf_stars.csv")

data = []

for row in df:
    data.append(row)

headers_data = data[0]
stars_data = data[1:]

for row in df:
    df = df[df[stars_data].notna()]

mass = float(data[3])
radius = float(data[4])

for i in mass:
    i *= 0.000954588

for i in radius:
    i *= 0.102763

##############################################################################

dataset_1 = []
dataset_2 = []

with open("dwarf_stars.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset_1.append(row)

with open("bright_stars.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset_2.append(row)

headers_1 = dataset_1[0]
stars_data_1 = dataset_1[1:]

headers_2 = dataset_2[0]
stars_data_2 = dataset_2[1:]

headers = headers_1 + headers_2

stars_data = []

for index, data_row in enumerate(stars_data_1):
    stars_data.append(stars_data_1[index] + stars_data_2[index])

with open("merged.csv", "a+") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(stars_data)