def rec_power(x, n):
    if n == 1 : return x
    if not n & 1:
        y = rec_power(x, n // 2)
        return y * y
    else:
        y = rec_power(x, (n - 1) // 2)
        return y * y * x
def iter_power(x, n):
    rst = 1
    for i in range(n):
        rst = rst * x
    return rst

print(rec_power(2, 1000000))
print(iter_power(2, 1000000))