
def fib(n: int) -> int:
    if n == 0 or n == 1:
        return n 
    else: 
        return fib(n-1) + fib(n-2)
    
for i in range(11):
    print(i, " fib-> ", fib(i))