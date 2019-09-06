import sys
sys.stdin = open("input.txt")

def cal(y, x):
    tp = 0
    for ty in range(M):
        for tx in range(M):
            tp += data[y+ty][x+tx]
    return tp
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        data[i] = list(map(int, input().split()))
    result = 0
    for y in range(N - M + 1):
        for x in range(N - M + 1):
            result = max(result, cal(y, x))
    print("#{} {}" .format(tc , result))