import sys
sys.stdin = open("input.txt")

def makeset(x):
    if x != p[x]: p[x] = makeset(p[x])
    return p[x]
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    dl = [0] * M
    p = list(range(N+1))
    ret = N
    for i in range(M):
        data = list(map(int, input().split()))
        p1 = makeset(data[0])
        p2 = makeset(data[1])
        if p1 != p2:
            ret -= 1
            p[p2] = p1
    print("#{} {}".format(tc, ret))