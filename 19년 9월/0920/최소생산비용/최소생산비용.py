import sys
sys.stdin = open("input.txt")

def d(n, dep, sum):
    global my
    if my < sum:
        return
    if dep == N:
        my = min(my , sum)
        return
    for i in range(N):
        if visit[i] == 0:
            visit[i] = 1
            d(i, dep +1, sum + data[dep][i])
            visit[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        data[i] = list(map(int, input().split()))
    visit = [0] * N
    my = 987654321
    d(0, 0, 0)
    print("#{} {}".format(tc, my))