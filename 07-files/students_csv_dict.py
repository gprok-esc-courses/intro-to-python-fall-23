import csv 

file = open("students.csv")

csvreader = csv.DictReader(file)

for row in csvreader:
    print(row)