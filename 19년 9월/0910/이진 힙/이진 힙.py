import sys
sys.stdin = open("input.txt")

def t(a, tmp):
    nod[a][2] = tmp
    pu = tmp
    if pu < nod[nod[a][3]][2]:
        nod[a][2] = nod[nod[a][3]][2]
        t(nod[a][3], pu)
def result(a):
    if nod[a][3]:
        return result(nod[a][3]) + nod[a][2]
    return nod[a][2]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    nod = [[0 for _ in range(4)] for _ in range(N+1)]
    d, i = 2, 1
    while (d < N+1):
        if nod[i][1]:
            i += 1
        nod[d][3] = i
        if nod[i][0]:
            nod[i][1] = d
        else:
            nod[i][0] = d
        d += 1
    for k in range(1, N+1):
        t(k, data[k-1])
    print("#{} {}".format(tc, result(nod[N][3])))