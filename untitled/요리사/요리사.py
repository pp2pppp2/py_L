import sys
sys.stdin = open("input.txt")

def cal():
    ret1 = 0
    ret2 = 0
    for y in range(N):
        for x in range(N):
            if c[y] == c[x] == 1 and y != x:
                ret1 += ing[y][x]
            elif c[y] == c[x] == 2 and y != x:
                ret2 += ing[y][x]
    return abs(ret1 - ret2)

def d(cnt):
    global ret
    if cnt == N:
        ret = min(ret, cal())
        return
    for i in range(2):
        if S[i] != 0:
            S[i] -= 1
            c[cnt] = i+1
            d(cnt+1)
            c[cnt] = 0
            S[i] += 1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    S = [N // 2] * 2
    c = [0] * N
    ret = 987654321
    ing = [list(map(int, input().split())) for _ in range(N)]
    d(0)
    print("#{} {}" .format(tc, ret))