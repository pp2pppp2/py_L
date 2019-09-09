import sys
sys.stdin = open("input.txt")
def d(i,j):
    m = str(data[i] * data[j])
    for k in range(len(m) - 1):
        if m[k] > m[k + 1]: break
    else: return int(m)
    return -1
T = int(input())
for tc in range(1, T+1):
    N , result = int(input()) , -1
    data = list(map(int, input().split()))
    for i in range(N):
        for j in range(i+1, N):
            result = max(result, d(i, j))
    print("#{} {}".format(tc, result))