
data = [1, 2, 3, 4, 5]

data_increased = list(map(lambda v : v+1, data))

print(data_increased)

data_increased = []
for v in data:
    data_increased.append(v+1)

print(data_increased)

def increase(v):
    return v+1

data_increased = list(map(lambda v : increase(v), data))

print(data_increased)