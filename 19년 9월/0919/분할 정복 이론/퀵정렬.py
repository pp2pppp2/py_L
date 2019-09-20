import sys
sys.stdin = open("input.txt")

def qu(m, l, r):
    p = m[l]
    i = l
    j = r
    while i < j:
        while m[i] <= p and i < r: i += 1
        while m[j] >= p and j > l: j -= 1
        if i < j: m[i], m[j] = m[j], m[i]
    m[l], m[j] = m[j], m[l]
    return j

def quu(m, l, r):
    if l > N//2:
        return
    if l < r:
        s = qu(m, l, r)
        quu(m, l, s - 1)
        quu(m, s + 1, r)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    m = list(map(int, input().split()))
    quu(m, 0, len(m)- 1)
    print(m)
    print("#{} {}" .format(tc,m[N // 2]))