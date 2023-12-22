import random

def print_tree_base(tree_size: int, base_height: int) -> None:
    """
    Prints the base of the tree, using spaces and the # char.
    """
    for x in range(base_height):
        for i in range(tree_size // 2):
            print(' ', end='')
        print('#')

def print_spaces(spaces: int) -> None:
    for s in range(spaces):
        print(' ', end='')

def print_asterisks(asterisks: int, probability: int) -> None:
    for a in range(asterisks):
        r = random.randint(1, 100)
        if r < probability:
            print('O', end='')
        else:
            print('*', end='')

def print_tree_row(spaces: int, asterisks: int, probability: int) -> None:
    print_spaces(spaces)
    print_asterisks(asterisks, probability)
    print()

try: 
    n = int(input("Give tree size: "))
    probability = int(input("Give tree decoration (1 - 100): "))
except ValueError:
    print("error, using default values, height=7, probability=20%")
    n = 7
    probability = 20

if n % 2 == 0:
    n -= 1

tree_height = n // 2 + 1
spaces = n // 2
asterisks = 1

# Repeat lines times
    # Repeat spaces times and print 1 space
    # Repeat asterisks times and print 1 asterisk
    # Reduce spaces by 1
    # Increase asterisks by 2

for i in range(tree_height):
    print_tree_row(spaces, asterisks, probability)
    spaces -= 1
    asterisks += 2

print_tree_base(n, 2)
