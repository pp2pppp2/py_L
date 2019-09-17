import sys
sys.stdin = open("input.txt")

def d(h, dep, x):
    global mt
    if dep == N - 1:
        if mt < h:
            mt = h
        return
    if m[dep][x] > h:
        return
    else:
        m[dep][x] = h
    for i in range(N):
        if visit[i] == 0:
            visit[i] = 1
            d(h * data[dep][i] / 100, dep+1, i)
            visit[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [[0 for _ in range(N)] for _ in range(N)]
    m = [[-1 for i in range(N)] for j in range(N)]
    for i in range(N):
        data[i] = list(map(int, input().split()))
    mt = 0
    visit = [0] * N
    for i in range(N):
        visit[i] = 1
        d(1 * data[0][i] / 100, 0, i)
        visit[i] = 0
    print("#{} {}".format(tc, mt*100))