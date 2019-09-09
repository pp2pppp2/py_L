import sys
sys.stdin = open("input.txt")

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def w(y, x):
    global N
    if x < 0 or x > N - 1 or y < 0 or y > N - 1 or data[y][x] == 1 or visit[y][x]:
        return False
    return True

def s(y,x):
    visit[y][x] = 1
    if r[0] == 1:
        return
    if data[y][x] == 2:
        r[0] = 1
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if w(ty, tx):
            s(ty, tx)
    return
def v(N):
    for y in range(N):
        for x in range(N):
            if data[y][x] == 3:
                s(y,x)
                return

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [[0 for _ in range(N)] for _ in range(N)]
    visit = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        data[i] = list(map(int,input()))
    r = [0]
    v(N)
    print("#{} {}" .format(tc, r[0]))