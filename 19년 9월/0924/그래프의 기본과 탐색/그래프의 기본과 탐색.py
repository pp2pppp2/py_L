import sys
sys.stdin = open("input.txt")

def makeset(x):
    if x == p[x]: return x
    else: return makeset(p[x])
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    data = list(map(int, input().split()))
    dl = [0] * E
    p = list(range(V+1))
    ret = V
    for i in range(E):
        p1 = makeset(data[i * 2])
        p2 = makeset(data[i * 2 + 1])
        if p1 != p2:
            ret -= 1
            p[p2] = p1
    print("#{} {}".format(tc, ret))