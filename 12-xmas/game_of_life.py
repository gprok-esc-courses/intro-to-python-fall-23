import random
from typing import List

def print_current_generation(current: List[List]) -> None:
    size = len(current)
    for r in range(size):
        for c in range(size):
            ch = '-' if current[r][c] == 0 else 'X'
            print(ch, end=' ')
        print()

def get_neighbours(current: List[List], row: int, col: int) -> int:
    total = 0
    size = len(current)
    for r in range(row-1, row+2):
        for c in range(col-1, col+2):
            if r >= 0 and c < size and r < size and col >= 0:
                total += current[r][c]
    total -= current[row][col]

    return total


def calculate_next(next: List[List], current: List[List]) -> None:
    size = len(current)
    for r in range(size):
        for c in range(size):
            n = get_neighbours(current, r, c)
            if current[r][c] == 1:
                if n < 2 or n > 3:
                    next[r][c] = 0
                else:
                    next[r][c] = 1
            else:
                if n == 3:
                    next[r][c] = 1
                else:
                    next[r][c] = 0

def copy_next_to_current(next: List[List], current: List[List]) -> None:
    size = len(current)
    for r in range(size):
        for c in range(size):
            current[r][c] = next[r][c]


generation = 1
size = 10
probability = 60

current = []
next = [] 

# Intialize grids
for r in range(size):
    rowc = []
    rown = []
    for c in range(size):
        r = random.randint(0,100)
        rowc.append(1 if r < probability else 0)
        rown.append(0)
    current.append(rowc)
    next.append(rown)



# Repeat
    # print current
    # ask user to continue (if not break)
    # calculate next generation
    # copy next to current

while True:
    print()
    print_current_generation(current)
    answer = input("Continue? (y/n): ")
    if answer == 'n':
        break
    calculate_next(next, current)
    copy_next_to_current(next, current)


