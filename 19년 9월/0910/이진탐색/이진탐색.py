import sys
sys.stdin = open("input.txt")

def f(a):
    global c, r, re
    if a:
        f(nod[a][0])
        c += 1
        if a == 1: r = c
        if a == N // 2: re = c
        f(nod[a][1])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nod = [[0 for _ in range(2)] for _ in range(1001)]
    d, i, c = 2, 1, 0
    while (d < N+1):
        if nod[i][1]:
            i += 1
        if nod[i][0]:
            nod[i][1] = d
        else:
            nod[i][0] = d
        d += 1
    f(1)
    print("#{} {} {}".format(tc, r, re))