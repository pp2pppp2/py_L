import sys
sys.stdin = open("input.txt")

def d(x, y, sum):
    global ret, con
    if x == y == N - 1:
        print(x, y)
        if ret > sum:
            ret = sum
    if m[y][x] == -1:
        m[y][x] = sum
    elif m[y][x] <= sum:
        return
    for i in range(2):
        tx = x + dx[i]
        ty = y + dy[i]
        if tx < N and ty < N:
            d(tx, ty, sum +data[ty][tx])

dx = [0, 1]
dy = [1, 0]

T= int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [[0 for _ in range(N)] for _ in range(N)]
    m = [[-1 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        data[i] = list(map(int, input().split()))
    ret = 987654321
    con = 0
    d(0, 0, data[0][0])
    print(ret, con)