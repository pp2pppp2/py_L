import sys
sys.stdin = open("input.txt")

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(y , x):
    global result
    q = [(y,x)]
    visit[y][x] = 1
    while q:
        t = q.pop(0)
        if data[t[0]][t[1]] == 3:
            result = 1
        for i in range(4):
            ty = t[0] + dy[i]
            tx = t[1] + dx[i]
            if data[ty][tx] != 1 and visit[ty][tx] == 0:
                visit[ty][tx] = 1
                q.append((ty , tx))


for tc in range(1,11):
    T = int(input())
    data = [[0 for _ in range(100)] for _ in range(100)]
    visit = [[0 for _ in range(100)] for _ in range(100)]
    for i in range(100):
        data[i] = list(map(int,input()))
    result = 0
    for y in range(100):
        for x in range(100):
            if data[y][x] == 2:
                bfs(y , x)
    print("#{} {}" .format(tc, result))