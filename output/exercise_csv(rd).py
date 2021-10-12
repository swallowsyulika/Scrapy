import csv

csvfile = "Example.csv"
with open(csvfile, "r") as rd:
    reader = csv.reader(rd)
    for row in reader:
        print(','.join(row))
