
def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    else:
        f = 1
        for i in range(2, n+1):
            f *= i 
        return f 
    
def factorial_recursive(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    else:
        return factorial_recursive(n-1) * n
    
if __name__ == "__main__":
    print(factorial_recursive(5000))