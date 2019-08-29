import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(T):
    data = [0] * 2
    data = list (map (int , input().split()))
    t = [0] * 12
    n = len(t)
    cnt = [0,0]
    for i in range(n):
        t[i] = i+1
    for i in range(1 << n):
        tmp = 0
        cnt[0] = 0
        for j in range(n):
            if i & (1 << j):
                tmp += t[j]
                cnt[0] += 1
        if cnt[0] == data[0] and tmp == data[1]:
            cnt[1] += 1
    print("#{} {}" .format(tc+1,cnt[1]))