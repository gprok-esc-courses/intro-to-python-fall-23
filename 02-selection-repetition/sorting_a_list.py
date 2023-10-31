import random

items = int(input("How many items: "))
values = []

for i in range(items):
    values.append(random.randint(1, 1000))

print(values)

# Sort the list without using sorted() function
# Use the bubblesort algorithm

for i in range(len(values) - 1, 0, -1):
    for j in range(i):
        if values[j] > values[j+1]:
            values[j], values[j+1] = values[j+1], values[j]
            # Swaps values, instead of the following in any other language
            # temp = values[j]
            # values[j] = values[j+1]
            # values[j+1] = temp

print(values)