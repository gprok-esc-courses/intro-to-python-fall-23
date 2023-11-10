import random
from prime import is_prime

n = random.randint(1, 1000)

print(n)
if is_prime(n):
    print("OK")
else:
    print("Not OK")