# Extract digits from an integer
from typing import List

def extract_digits(n: int) -> List[int]:
    result = []
    value = n
    while value != 0:
        result.append(value % 10)
        value = value // 10
    return list(reversed(result))


print(extract_digits(2087))