import sys
sys.stdin = open("input.txt")

def s(cnt):
    global N , su , res
    if su > res:
        return
    if cnt == N:
        if su < res:
            res = su
        return
    for i in range(N):
        if visit[i] == 0:
            visit[i] = 1
            su += data[cnt][i]
            s(cnt + 1)
            su -= data[cnt][i]
            visit[i] = 0
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [[0 for _ in range(N)] for _ in range(N)]
    visit = [0 for _ in range(N)]
    for i in range(N):
        data[i] = list(map(int,input().split()))
    su = 0
    res = 987654321
    s(0)
    print("#{} {}".format(tc , res))