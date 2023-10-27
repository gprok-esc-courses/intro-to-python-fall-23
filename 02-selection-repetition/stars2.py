n = int(input("Give a number: "))

for i in range(n):
    for j in range(i+1):
        print('*', end=' ')
    print()