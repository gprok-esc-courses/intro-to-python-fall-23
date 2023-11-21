import random

data = []
for i in range(1000):
    v = random.randint(1, 100)
    data.append(v)

counters = {}

for v in data:
    if v in counters:
        counters[v] += 1
    else:
        counters[v] = 1

sorted_counters_by_keys = dict(sorted(counters.items()))

for c in sorted_counters_by_keys:
    print(c, sorted_counters_by_keys[c])
