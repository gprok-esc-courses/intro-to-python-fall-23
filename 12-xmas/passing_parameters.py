from typing import List

def change_values(v: int, d: List) -> None:
    v = v + 1
    for i in range(len(d)):
        d[i] += 1


data = [1,2,3,4,5]
value = 5

change_values(value, data)

print(value)
print(data)

