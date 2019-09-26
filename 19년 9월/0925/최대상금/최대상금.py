import sys
sys.stdin = open("input.txt")

def d(n, k, dep):
    global ma, ret
    if dep - 1== int(M):
        return
    if RN == ma:
        return
    if ma < ''.join(N) and dep - 1 < int(M):
        ma = ''.join(N)
        ret = dep
    for i in range(k, n):
        if N[i] > N[k]:
            N[i], N[k] = N[k], N[i]
            d(n, k + 1, dep + 1)
            N[i], N[k] = N[k], N[i]
        else:
            d(n, k + 1, dep)
T = int(input())
for tc in range(1, T+1):
    N, M = input().split()
    vi = [0] * 10
    t = 0
    for i in range(len(N)):
        if vi[int(N[i])] == 0:
            vi[int(N[i])] += 1
        else:
            t = 1
            break
    N = list(N)
    RN = ''.join(reversed(sorted(N)))
    ma = ''.join(N)
    d(len(N), 0, 0)
    if (int(M) - ret) // 2 and t == 0:
        ma = list(ma)
        ma[-2], ma[-1] = ma[-1], ma[-2]
        ma = ''.join(ma)
    print("#{} {}" .format(tc, ma))
