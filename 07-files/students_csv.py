import csv 

file = open("students.csv")

csvreader = csv.reader(file)

for row in csvreader:
    print(row)