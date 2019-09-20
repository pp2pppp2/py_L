import sys
sys.stdin = open("input.txt")

def d(num, dep):
    global mi
    if dep > mi:
        return
    if num > N-1:
        if mi > dep:
            mi = dep
        return
    for i in range(M[num], 0 , -1):
        d(num + i, dep + 1)

T = int(input())
for tc in range(1, T+1):
    M = list(map(int, input().split()))
    N = M[0]
    mi = 9999
    d(1, -1)
    print('#{} {}'.format(tc, mi))