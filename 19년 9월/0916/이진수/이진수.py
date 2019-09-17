import sys
sys.stdin = open("input.txt")

h = [0] * 16
for i in range(16):
    out = ''
    for j in range(3, -1, -1):
        out += '1' if i & (1 << j) else '0'
    h[i] = out
T = int(input())
for tc in range(1, T+1):
    N, data = list(input().split())
    re = ''
    for i in data:
        if i >= 'A':
            re += h[ord(i) - ord('A')+10]
        else:
            re += h[ord(i) - ord('0')]
    print("#{} {}" .format(tc,re))