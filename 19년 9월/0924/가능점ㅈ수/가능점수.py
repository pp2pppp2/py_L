import sys
sys.stdin = open("input.txt")

def d(a, dep, sum):
    if dep <= N:
        b.add(sum)
    for i in range(a, len(E)):
        if visit[i] == 0:
            visit[i] = 1
            d(i, dep +1, sum + E[i])
            visit[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    E = list(map(int, input().split()))
    cnt = [0] * 101
    ret = len(E)
    for i in range(0, N):
        cnt[i] += 1
    print(ret + 1)
    visit = [0] * len(E)
    b = set()
    d(0, 0, 0)
    print(len(b))
