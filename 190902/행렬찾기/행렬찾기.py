import sys

sys.stdin = open("input.txt")


from functools import cmp_to_key
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def dfs(y , x , cnt):
    visit[y][x] = cnt
    sc[cnt] += 1
    q = [(y, x)]
    while q:
        t = q.pop(0)
        for i in range(4):
            tx = t[1] + dx[i]
            ty = t[0] + dy[i]
            if tx > -1 and tx < N and ty > -1 and ty < N and data[ty][tx] <10 and data[ty][tx] > 0 and visit[ty][tx] == 0:
                q.append((ty, tx))
                visit[ty][tx] = cnt
                sc[cnt] += 1

def compare(x , y):
    if x == 0 or y == 0:
        return 0
    if x[2] > y[2]:
        return 1
    elif x[2] < y[2]:
        return -1
    else:
        if x[0] > y[0]:
            return 1
        else:
            return -1


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    data = [ [0 for _ in range(N)] for _ in range(N)]
    visit = [ [0 for _ in range(N)] for _ in range(N)]
    sc = [0] * 30
    for i in range(N):
        data[i] = list(map(int, input().split()))
    cnt = 10
    for y in range(N):
        for x in range(N):
            if data[y][x] > 0 and data[y][x] < 10 and visit[y][x] == 0:
                dfs(y, x, cnt)
                cnt += 1
    lu = [0] * 2
    rd = [0] * 2
    for i in range(10 , cnt):
        tmp = sc[i]
        for y in range(N):
            for x in range(N):
                if visit[y][x] == i:
                    lu = [y, x, visit[y][x]]
                if visit[N -1 - y][N - 1 - x] == i:
                    rd = [N -1 - y, N - 1 - x, visit[N -1 - y][N - 1 - x]]
                sc[i] = [lu[0] - rd[0] + 1,lu[1]- rd[1] + 1 , tmp]
    sc = sorted(sc, key=cmp_to_key(compare))
    print("#{} {}" .format(tc, cnt-10) ,end=" ")
    for i in range(10,cnt):
        print("{} {}" .format(sc[i][0] , sc[i][1]), end=" ")
    print()