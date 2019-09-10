import sys
sys.stdin = open("input.txt")

def go(a):
    global ret
    if a:
        go(nod[a][0])
        go(nod[a][1])
        nod[nod[a][3]][2] += nod[a][2]
    if a == L:
        ret = nod[a][2]
T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    nod = [[0 for _ in range(4)] for _ in range(N+1)]
    d, i = 2, 1
    while d < N+1:
        if nod[i][1]:
            i += 1
        nod[d][3] = i
        if nod[i][0]:
            nod[i][1] = d
        else:
            nod[i][0] = d
        d += 1
    for i in range(M):
        A, B = map(int, input().split())
        nod[A][2] = B
    go(1)
    print("#{} {}".format(tc, ret))