import sys
sys.stdin = open("input.txt")

dx = [1, -1, -1, 1]
dy = [1, 1, -1, -1]

def d(y, x, f):
    global ret
    if f == 4:
        if y == fy and x == fx:
            ret = max(visit[y][x], ret)
        return
    tx = x + dx[f]
    ty = y + dy[f]
    if 0 <= tx < N and 0 <= ty < N and visit[ty][tx] == 0 and v[cafe[ty][tx]] == 0:
        visit[ty][tx] = visit[y][x] + 1
        v[cafe[ty][tx]] = 1
        d(ty, tx, f)
        d(ty, tx, f+1)
        visit[ty][tx] = 0
        v[cafe[ty][tx]] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0] * N for _ in range(N)]
    v = [0] * 101
    ret = 0
    for y in range(N):
        for x in range(N):
            fx = x
            fy = y
            d(y, x, 0)
    if ret < 4:
        ret = -1
    print("#{} {}" .format(tc, ret))