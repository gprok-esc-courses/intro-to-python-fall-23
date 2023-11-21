
from functools import reduce


data = [1, 2, 3, 4, 5]

def test(a, b):
    print(a, b)
    return (a * b)

total = reduce(lambda a, b: test(a, b), data)

print(total)