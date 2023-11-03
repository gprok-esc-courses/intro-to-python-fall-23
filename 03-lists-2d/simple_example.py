
matrix = [
    [10, 11, 12, 13],
    [14, 15, 16, 17, 45, 36],
    [18, 19, 20, 21],
    [18, 19],
    [18, 19, 20, 21]
]

print(len(matrix))
print(len(matrix[0]))

for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        print(matrix[row][col], end=' ')
    print()