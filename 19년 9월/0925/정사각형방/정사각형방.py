import sys
sys.stdin = open("input.txt")

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def b(y, x):
    global ret, re
    q = [[y, x, 0]]
    qsz = 1
    idx = 0
    while qsz > idx:
        t = q[idx]
        idx += 1
        if nu[t[0]][t[1]] == -1:
            nu[t[0]][t[1]] = t[2]
        elif nu[t[0]][t[1]] > t[2]:
            continue
        for i in range(4):
            tx = t[1] + dx[i]
            ty = t[0] + dy[i]
            if 0 <= tx < N and 0 <= ty < N and data[ty][tx] - data[t[0]][t[1]] == 1:
                q.append([ty, tx, t[2] + 1])
                qsz += 1
    if ret == qsz:
        re = min(re, data[y][x])
    elif ret < qsz:
        ret = qsz
        re = data[y][x]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [[0 for _ in range(N)] for _ in range(N)]
    nu = [[-1 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        data[i] = list(map(int, input().split()))
    ret = 0
    re = 987654321
    for y in range(N):
        for x in range(N):
            b(y, x)
    print("#{} {} {}" .format(tc, re, ret))