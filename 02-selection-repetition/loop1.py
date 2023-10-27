
for i in range(10):
    print(i)
print("==============")
for i in range(3, 10):
    print(i)
print("==============")
for i in range(1, 10, 3):
    print(i)
print("==============")
for i in range(10, 3, -1):
    print(i)
print("==============")

ans = 'y'
while ans == 'y':
    print("In the loop 1")
    ans = input("Continue, y or n? ")

while True:
    print("In the loop 2")
    ans = input("Continue, y or n? ")
    if ans == 'n':
        break

