def myprint(q):
    for i in range(q-1, -1, -1):
        print("%d " % t[i], end="")
    print()

def comb(n, r, q):
    if r == 0:
        myprint(q)
    elif n < r:
        return
    else:
        t[r-1] = a[n-1]
        comb(n-1, r-1, q)
        comb(n-1, r, q)

a =[4, 3, 2, 1]
t = [0] * 3

comb(4, 3, 3)