def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-2) + fibo(n-1)
def fibo2(n):
    f =[0, 1]
    for i in range(2, n+1):
        f.append(f[i-1]+ f[i-2])
    return f[n]
print(fibo2(1000))