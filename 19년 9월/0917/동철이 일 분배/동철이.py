import sys
sys.stdin = open("input.txt")
def s(a):
    return int(a)/ 100
def d(h, dep, x, sum):
    global mt, cmc, cnt
    if mt >= h:
        return
    if dep == N:
        if mt < h:
            mt = h
        return
    # if dep < 4:
    #     if not cm.get(sum):
    #         cm[sum] = cmc
    #         cmc += 1
    #     else:
    #         if m[cm[sum]][dep][x] >= h:
    #             return
    #         else:
    #             m[cm[sum]][dep][x] = h
    for i in range(N):
        if visit[i] == 0 and not data[dep][i] == 0:
            visit[i] = 1
            d(h * data[dep][i] / 100, dep+1, i, sum + 2 ** i)
            visit[i] = 0
    cnt +=1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [[0 for _ in range(N)] for _ in range(N)]
    m = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(3000)]
    cm = {}
    cmc = 1
    for i in range(N):
        data[i] = list(map(int, input().split()))
    mt = 0
    cnt = 0
    arr = []
    visit = [0] * N
    d(100, 0, 0, 0)
    print("#%d" % tc , end=" ")
    print("%.6f" % mt)
    print(cnt)