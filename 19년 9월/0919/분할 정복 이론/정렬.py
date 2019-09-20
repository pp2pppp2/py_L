import sys
sys.stdin = open('input.txt')

def merge(l, r):
    global cnt
    result = []
    lc = 0
    rc = 0
    while len(l) > lc or len(r) > rc:
        if len(l) > lc and len(r) > rc:
            if l[lc] <= r[rc]:
                result += [l[lc]]
                lc += 1
            else:
                result += [r[rc]]
                rc += 1
        elif len(l) > lc:
            result += [l[lc]]
            lc += 1
        elif len(r) > rc:
            result += [r[rc]]
            rc += 1
    return result
def mersort(m):
    global cnt
    if len(m) == 1: return m
    l, r = [], []
    mid = len(m) // 2
    l = m[0: mid]
    r = m[mid: len(m)]
    l = mersort(l)
    r = mersort(r)
    if len(l) and len(r) and l[-1] > r[-1]:
        cnt += 1
    return merge(l, r)
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = 0
    m = list(map(int, input().split()))
    print("#{} {} {}".format(tc, mersort(m)[N // 2], cnt))