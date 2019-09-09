import sys
sys.stdin = open("input.txt")
from functools import cmp_to_key

def co(i , j):
    return abs(coh[i][0] - coh[j][0]) + abs(coh[i][1] - coh[j][1])

def compare(a, b):
    return abs(h[0] - b[0]) + abs(h[1] - b[1]) > abs(h[0] - a[0]) + abs(h[1] - a[1])

def d(a, cnt):
    global s, ret
    if s + min(nod[N+1]) > ret:
        return
    if cnt == N+1:
        s += nod[a][N+1]
        if ret > s:
            ret = s
        s -= nod[a][N+1]
        return
    for i in range(1, N+1):
        if visit[i] == 0:
            visit[i] = 1
            s += nod[a][i]
            d(i, cnt+1)
            s -= nod[a][i]
            visit[i] = 0
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    m = list(map(int,input().split()))
    nod = [[0 for _ in range(N+2)] for _ in range(N+2)]
    visit = [0] * (N+2)
    h = [[m[0], m[1]]]
    coh = [[m[0], m[1]]]
    for i in range(4, len(m), 2):
        coh += [[m[i],m[i+1]]]
    coh += [[m[2], m[3]]]
    for i in range(N+2):
        for j in range(i+1, N+2):
            nod[i][j] = co(i, j)
            nod[j][i] = nod[i][j]
    ret = 987654321
    visit[0] = 1
    for i in range(0,N+1):
        s = 0
        visit[i] = 1
        d(0, 1)
        visit[i] = 0

    print("#{} {}".format(tc,ret))