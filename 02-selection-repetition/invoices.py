# Ask user to give number of invoices
# Fill a list with random numbers 1-1000 (as many as the number of invoices)
# Find max, min, total, and average

import random

invoice_number = int(input("How many invloces: "))
amounts = []

for i in range(invoice_number):
    amounts.append(random.randint(1, 1000))

print(amounts)

max_value = 0
min_value = float('inf')
total = 0
for i in range(invoice_number):
    if amounts[i] > max_value:
        max_value = amounts[i]
    if amounts[i] < min_value:
        min_value = amounts[i]
    total += amounts[i]

print("Max:", max_value)
print("Min:", min_value)
print("Total:", total)
print("Avg:", total/invoice_number)

print("===> THE PYTHON WAY")
print(max(amounts))
print(min(amounts))
total = sum(amounts)
print(total)
print(total/invoice_number)

# Print list sorted
print(sorted(amounts, reverse=True))
print(amounts)
