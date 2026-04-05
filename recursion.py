def counting(n);
    
    if n==0:
        return
    print(n)
    counting(n-1)

counting(10)

def fib(n)
    if n==0 or n==1:
        return n
    return fib(n-1)+fib(n-2)

print(fib(8))

def sum_natural(n):
    if n==1 or n==0:
        return n
    
    return n + sum_natural(n-1)

print(sum_natural(5))