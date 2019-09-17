def myprint(q):
    for i in range(q-1, -1, -1):
        print("%d " % t[i], end="")
    print()

def perm(n, r, q):
    if r==0:
        myprint(q)
    else:
        for i in range(n-1, -1, -1):
            a[i], a[n - 1] = a[n-1], a[i]
            t[r-1] = a[n-1]
            perm(n, r-1, q)
            a[n - 1], a[i] = a[i], a[n - 1]

a = [3, 2, 1]
t = [0] * 3

perm(3, 3, 3)