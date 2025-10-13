def f(n):
    if n==0:
        return
    
    k = f(n-1)
    return n + k

n = 10
print(f(n))