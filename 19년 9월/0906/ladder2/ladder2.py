import sys
import time
from time import strftime
start_time = time.time()
sys.stdin = open("input.txt")
dx = [1, -1, 0]
dy = [0, 0, 1]
def s(y, x, cnt):
    global mct, result, ss
    if y == 99:
        if mct >= cnt:
            result = ss
            mct = cnt
        return
    if cnt > mct:
        return
    for i in range(3):
        tx = x + dx[i]
        ty = y + dy[i]
        if 0<= tx < 100 and ty < 100 and v[ty][tx] ==0 and m[ty][tx] == 1:
            v[ty][tx] = 1
            s(ty, tx, cnt+1)
            return
for tc in range(1, 11):
    t = int(input())
    m = [list(map(int,input().split())) for _ in range(100)]
    mct = 987654321
    result =0
    for i in range(100):
        if m[0][i] == 1:
            v = [[0 for _ in range(100)] for _ in range(100)]
            ss = i
            s(0, i, 0)
    print("#{} {}" .format(tc, result))
print(time.time() - start_time, 'seconds')