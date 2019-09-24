import sys
sys.stdin = open("input.txt")

T = int(input())
arr = [0, 1, -1, -10]
def d():
    q = [[0] for _ in range(100000)]
    qsiz = 1
    q[0] = [N, 0]
    ret = 3000
    idx = 0
    while qsiz > idx:
        t = q[idx % 100000]
        idx += 1
        arr[0] = t[0]
        if t[0] == M:
            return t[1]
        for i in range(4):
            a = t[0]+arr[i]
            if ret < t[1] or a < 0 or a > M+M//2:
                continue
            if visit[a] == 0:
                visit[a] = 1
                q[qsiz % 100000] = [a, t[1] + 1]
                qsiz += 1
for tc in range(1, T+1):
    N, M = map(int, input().split())
    visit = [0] * 2000001
    print("#{} {}".format(tc, d()))