import sys
sys.stdin = open("input.txt")

dy = [0, 1, -1]

def move(y , x):
    global result
    ty = y + dy[m[y][x]]
    if ty == -1 or ty == 100:
        m[y][x] = 0
        return
    if m[ty][x] == 0:
        m[ty][x] , m[y][x] = m[y][x] , 0
        return
    if m[ty][x] == m[y][x] or m[ty][x] == 999:
        m[y][x] = 999
        return
    if m[ty][x] != m[y][x]:
        m[ty][x] = 999
        m[y][x] = 999
        result += 1


for tc in range(1,11):
    N = int(input())
    m = [[0 for _ in range(100)] for _ in range(100)]

    for i in range(N):
        m[i] = list(map(int,input().split()))
    result = 0
    t = 0
    while(t == 0):
        cnt = 0
        for y in range(N):
            for x in range(N):
                if m[y][x] == 1:
                    move(y,x)
                    cnt += 1
                if m[99-y][x] == 2:
                    move(99-y,x)
                    cnt += 1
        if cnt == 0:
            t += 1
    print("#{} {}" .format(tc, result))