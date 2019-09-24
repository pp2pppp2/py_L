import sys
sys.stdin = open("input.txt")

def d(a, sum):
    global ret
    if sum >= B:
        if sum < ret:
            ret = sum
    for i in range(a , -1 , -1):
        if visit[i] == 0:
            visit[i] = 1
            d(i, sum + data[i])
            visit[i] = 0

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    data = sorted(list(map(int, input().split())))
    visit = [0] * N
    ret = 987654321
    d(N-1, 0)
    print("#{} {}" .format(tc, ret-B))