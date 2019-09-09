import sys
sys.stdin = open("input.txt")

dx = [0, 1]
dy = [1, 0]

def chk(y, x, i):
    global result
    tx = x + dx[i]
    ty = y + dy[i]
    leng = 0
    while 0 <= tx < N and 0 <= ty < N and data[ty][tx] != 0:
        leng += 1
        tx += dx[i]
        ty += dy[i]
    if leng == K-1:
        result += 1

T = int(input())
for tc in range(1,T+1):
    N, K = map(int, input().split())
    data = [[0 for _ in range(N+2)] for _ in range(N+2)]
    for i in range(1,N+1):
        data[i] = list(map(int, input().split()))
    result = 0
    for y in range(N):
        for x in range(N):
            for a in range(2):
                if (y == 0 or data[y - 1 + a][x - a] == 0)and data[y][x] == 1:
                    chk(y, x, a)
    print("#{} {}" .format(tc, result))