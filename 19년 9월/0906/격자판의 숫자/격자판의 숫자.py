import sys
sys.stdin = open("input.txt")

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def s(y, x, cnt, d, t):
    global result, ccnt
    if cnt == 6:
        ts = "".join(t)
        result.append(ts)
        return
    if v[y][x][d][cnt] == t:
        return
    v[y][x][d][cnt] = list(t)
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if 0<= tx < 4 and 0<= ty < 4:
            s(ty, tx, cnt+1, i, t + [m[ty][tx]])

T = int(input())
for tc in range(1, T+1):
    m = [list(input().split()) for _ in range(4)]
    v = [[[[[-1 for i in range(1)] for _ in range(8)] for _ in range(4)] for _ in range(4)] for _ in range(4)]
    t = []
    result = []
    ccnt = 0
    for y in range(4):
        for x in range(4):
            s(y,x,0, 0, [m[y][x]])
    print("#{} {}" .format(tc, len(set(result))))

