import sys
sys.stdin = open("input.txt")

d = ['up', 'down', 'left', 'right']
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def p(dn):
    a = dn % 2
    for i in range(3):
        for y in t[a]:
            for x in t[a]:
                ty, tx = y + dy[dn], x + dx[dn]
                if i == 1 and 0 <= tx < N and 0 <= ty < N and data[ty][tx] == data[y][x]:
                    data[y][x], data[ty][tx] = data[y][x]*2, 0
                elif data[y][x] == 0:
                    while 0 <= tx < N and 0 <= ty < N:
                        if data[ty][tx] != 0:
                            data[y][x], data[ty][tx] = data[ty][tx], data[y][x]
                            break
                        else:
                            ty += dy[dn]
                            tx += dx[dn]

for tc in range(int(input())):
    N, s = input().split()
    N = int(N)
    data = [list(map(int, input().split())) for _ in range(N)]
    dn = d.index(s)
    t = [range(N),range(N-1,-1,-1)]
    p(dn)
    print("#{}" .format(tc+1))
    for y in range(N):
        for x in range(N):
            print(data[y][x], end=" ")
        print()