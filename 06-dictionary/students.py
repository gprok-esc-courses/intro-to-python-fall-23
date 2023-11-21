
students = {}

students[1001] = {'name': 'John', 'gpa': 3.2, 'email': 'john@sch.ac'}
students[1002] = {'name': 'Mary', 'gpa': 2.6, 'email': 'mary@sch.ac'}
students[1003] = {'name': 'Tom', 'gpa': 3.7, 'email': 'tom@sch.ac'}

for sid in students:
    print(sid, students[sid]['name'])