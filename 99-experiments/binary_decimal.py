# Convert binary to decimal and decimal to binary

def decimal2binary(n: int) -> str:
    s = ''
    value = n
    while value != 0:
        remainder = value % 2
        s = str(remainder) + s 
        value = value // 2
    return s 

def binary2decimal(s: str) -> int:
    i = 0
    exp = 0
    for pos in range(len(s)-1, -1, -1):
        if s[pos] == '1':
            i = i + pow(2, exp)
        exp += 1
    return i


print(decimal2binary(189))
print(str(bin(189))[2:])

print(binary2decimal('10111101'))