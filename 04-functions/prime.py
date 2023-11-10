
def is_prime(num: int) -> bool: 
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


if __name__ == "__main__":
    n = int(input("Give a number: "))

    for value in range(1, n+1):
        if is_prime(value):
            print(value)
