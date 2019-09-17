import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N = float(input())
    s = 1
    re = ''
    for i in range(14):
        if N == 0:
            print('#{} {}'.format(tc,re))
            break
        if N >= s / 2:
            N -= s / 2
            re += '1'
        else:
            re += '0'
        s /= 2
    else:
        print('#{} overflow'.format(tc))
