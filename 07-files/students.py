students_file = open("students.csv")

lines = students_file.readlines()

headers = lines[0].split(",")
data = lines[1:]

print(headers)
print(data)

students = {}

for line in data:
    values = line.split(",")
    student = {headers[1]: values[1], headers[2]: values[2], headers[3]: values[3], headers[4].strip(): float(values[4].strip())}
    students[values[0]] = student

print("=================")
print(students)

# Calculate class average
total = 0.0
for sid in students:
    total += students[sid]['gpa']

print("Average:", total/len(students))