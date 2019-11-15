import sys
sys.stdin = open("input.txt")

T = int(input())
def d(cnt, ret):
    global mi, ma
    if cnt == OC:
        mi = min(mi, ret)
        ma = max(ma, ret)
        return
    for i in range(len(O)):
        if O[i] != 0:
            O[i] -= 1
            if i == 0:
                d(cnt + 1, ret + Num[cnt + 1])
            elif i == 1:
                d(cnt + 1, ret - Num[cnt + 1])
            elif i == 2:
                d(cnt + 1, ret * Num[cnt + 1])
            elif i == 3:
                d(cnt + 1, int(ret / Num[cnt + 1]))
            O[i] += 1

for tc in range(1, T+1):
    N = int(input())
    O = list(map(int, input().split()))
    Num = list(map(int, input().split()))
    OC = sum(O)
    mi = 0xfffffff
    ma = -0xfffffff
    d(0, Num[0])
    print(ma - mi)
