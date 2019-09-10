import sys
sys.stdin = open("input.txt")

dx = [0, 0, 1, -1, 1, 1, -1, -1]
dy = [1, -1, 0, 0, -1, 1, -1, 1]

def d(x ,y, p):
    data[y][x] = p
    cnt[p % 2] += 1
    for i in range(8):
        tx = x + dx[i]
        ty = y + dy[i]
        if 0 <= tx < N and 0 <= ty < N and data[ty][tx] != 0 and data[ty][tx] != p:
            ttx = tx
            tty = ty
            go = 0
            while(0 <= ttx < N and 0 <= tty < N and data[tty][ttx] != 0):
                if data[tty][ttx] == p:
                    go = 1
                ttx += dx[i]
                tty += dy[i]
            if go:
                while(data[ty][tx] != p):
                    data[ty][tx] = p
                    cnt[p % 2] += 1
                    cnt[(p+1) % 2] -= 1
                    tx += dx[i]
                    ty += dy[i]


T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    data = [[0 for _ in range(N)] for _ in range(N)]
    cnt = [2, 2]
    data[N // 2 - 1][N // 2] = 1
    data[N // 2][N // 2 - 1] = 1
    data[N // 2][N // 2] = 2
    data[N // 2 - 1][N // 2 - 1] = 2
    for i in range(M):
        x , y , p = map(int, input().split())
        d(x-1, y-1, p)
    print("#{} {} {}" .format(tc, cnt[1], cnt[0]))