def comb(n, r):
    global cnt
    if r == 0:
        print(T)
        cnt += 1
    else:
        if n == 0 : return
        else:
            T[r-1] = A[n-1]
            comb(n,r-1)
            comb(n-1,r)

T = [0] * 3
A = range(1,201)
cnt = 0
comb(4,3)
print(cnt)

def comm(n,r):
    if r == 0:
        return 1
    elif n < r:
        return 0
    else:
         return comm(n-1, r-1) + comm(n-1, r)
print(comm(100,50))
