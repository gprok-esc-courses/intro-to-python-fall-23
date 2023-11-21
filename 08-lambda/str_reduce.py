
from functools import reduce


names = ["John", "Mike", "Peter", "Ann", "Mary"]

str = reduce(lambda s, name : s + ", " + name, names)

print(str)