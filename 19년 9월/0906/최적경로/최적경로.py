import sys
sys.stdin = open("input.txt")
from functools import cmp_to_key

def co(i , j):
    return abs(coh[i][0] - coh[j][0]) + abs(coh[i][1] - coh[j][1])

def compare(a, b):
    if abs(h[0][0] - b[0]) + abs(h[0][1] - b[1]) < abs(h[0][0] - a[0]) + abs(h[0][1] - a[1]):
        return 1
    else:
        return -1
def d(a, cnt, s):
    global ret
    if s + mmi > ret:
        return
    if cnt == N:
        s += nod[a][N+1]
        if ret > s:
            ret = s
        s -= nod[a][N+1]
        return
    for i in range(1, N+1):
        if visit[i] == 0:
            visit[i] = i
            d(i, cnt+1 , s + nod[a][i])
            visit[i] = 0
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    m = list(map(int,input().split()))
    nod = [[0 for _ in range(N+2)] for _ in range(N+2)]
    visit = [0] * (N+2)
    h = [[m[0], m[1]]]
    com = [[m[2], m[3]]]
    cohg = []
    coh = [[m[0], m[1]]]
    for i in range(4, len(m), 2):
        cohg += [[m[i], m[i + 1]]]
    coh += sorted(cohg, key=cmp_to_key(compare))
    coh += [[m[2], m[3]]]
    for i in range(N+2):
        for j in range(i+1, N+2):
            nod[i][j] = co(i, j)
            nod[j][i] = nod[i][j]
    ret = 987654321
    mmi = min(nod[N+1])
    for i in range(1,N+1):
        visit[i] = i
        d(i, 1, nod[i][0])
        visit[i] = 0

    print("#{} {}".format(tc,ret))