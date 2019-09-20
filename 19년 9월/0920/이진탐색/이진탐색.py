import sys
sys.stdin = open("input.txt")

def bs(A, l, r, key, d):
    global cnt
    if l > r:
        return
    else:
        m = (l + r) // 2
        if key == A[m]:
            cnt += 1
        elif A[m] < key and d != 2:
            bs(A, m + 1, r, key, 2)
        elif A[m] > key and d != 1:
            bs(A, l, m - 1, key, 1)
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    cnt = 0
    for i in B:
        bs(A, 0, N-1, i, 0)
    print("#{} {}" .format(tc, cnt))