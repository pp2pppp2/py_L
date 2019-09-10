import sys
sys.stdin = open("input.txt")

def d(a, qq):
    global result
    if a == A: tr[0] = 1
    if a == B: tr[1] = 1
    if N[a][2] != 0:
        qq = d(N[a][0], qq)
        if tr[0] == 1: N[a][3] += 1
        if tr[1] == 1: N[a][3] += 1
        qq = d(N[a][1], qq)
        if tr[1] == 1: N[a][3] += 1
        if N[a][3] == 2: result = a
        qq += 1
    return qq
T = int(input())
for tc in range(1, T+1):
    V, E, A, B = list(map(int, input().split()))
    data = list(map(int, input().split()))
    N = [[0 for _ in range(4)] for _ in range(V+1)]
    tr = [A, B]
    result = 0
    for i in range(0, len(data), 2):
        N[data[i]][2] = data[i]
        N[data[i+1]][2] = data[i+1]
        if N[data[i]][0] == 0:
            N[data[i]][0] = data[i+1]
        else:
            N[data[i]][1] = data[i+1]
    d(1, 0)
    print("#{} {} {}".format(tc, result, d(result, 0)))