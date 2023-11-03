
# data = []
# for i in range(100):
#     data.append(0)

data = [0]*100
data[5] = 67

print(data)

matrix = [[0]*10 for i in range(5)]
matrix[1][3] = 45
for row in matrix:
    print(row)