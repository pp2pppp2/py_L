import sys
sys.stdin = open("input.txt")

h = [0] * 62
tmp = [25, 19, 61, 35, 49, 47, 59, 55, 11]
for i in range(9):
    h[tmp[i]] = i+1
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    for i in range(N):
        d = input()
        if '1' in d:
            data = list(d)
    data.reverse()
    t = [0] * 8
    for i in range(M):
        if data[i] == '1':
            for j in range(8):
                for k in range(7):
                    t[j] += int(data[i + j * 7 + k]) * 2 ** k
            break
    t.reverse()
    result = 0
    for i in range(8):
        result += h[t[i]]
        if i % 2 == 0:
            result += h[t[i]] * 2
        t[i] = h[t[i]]
    if result % 10 == 0:
        print("#{} {}".format(tc, sum(t)))
    else:
        print("#{} 0".format(tc))