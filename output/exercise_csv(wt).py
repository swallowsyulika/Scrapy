import csv

csvfile = "Example2.csv"
li = [[1, 2, 3], [4, 5, 6]]
with open(csvfile, "w+", newline='') as wt:
    writer = csv.writer(wt)
    writer.writerow(['Data1', 'Data2', 'Data3'])
    for row in li:
        writer.writerow(row)
