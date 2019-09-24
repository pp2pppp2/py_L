import sys
sys.stdin = open("input.txt")

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

def b(ret):
    q = [[0, 0]]
    h[0][0] = 0
    while q:
        t = q.pop(0)
        for i in range(4):
            tx = t[1] + dx[i]
            ty = t[0] + dy[i]
            if 0 <= tx < N and 0 <= ty < N:
                if data[ty][tx] > data[t[0]][t[1]]:
                    if h[ty][tx] > data[ty][tx] - data[t[0]][t[1]] + h[t[0]][t[1]] + 1:
                        h[ty][tx] = data[ty][tx] - data[t[0]][t[1]] + h[t[0]][t[1]] + 1
                        q.append([ty, tx])
                else:
                    if h[ty][tx] > h[t[0]][t[1]] + 1:
                        h[ty][tx] = h[t[0]][t[1]] + 1
                        q.append([ty, tx])
    return h[N-1][N-1]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [[0 for _ in range(N)] for _ in range(N)]
    h = [[987654321 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        data[i] = list(map(int, input().split()))
    print("#{} {}" .format(tc,b(0)))