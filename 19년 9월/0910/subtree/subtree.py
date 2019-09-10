import sys
sys.stdin = open("input.txt")

def d(a, ret):
    if a:
        ret = d(n[a][0], ret)
        ret = d(n[a][1], ret)
        ret += 1
    return ret
T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    nod = list(map(int, input().split()))
    n = [[0 for _ in range(3)] for _ in range(E+2)]
    for i in range(0, E*2, 2):
        if n[nod[i]][0]:
            n[nod[i]][1] = nod[i+1]
        else:
            n[nod[i]][0] = nod[i+1]
    print("#{} {}".format(tc, d(N, 0)))