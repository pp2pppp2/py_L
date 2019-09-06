import sys
sys.stdin = open("input.txt")

dx = [0, -1 , 0]
dy = [-1, 0 , 1]
mx = [1, 0, -1]
my = [0, -1, 0]

def mprint(y, x, dn):
    print(data[y][x],end="")
    ty = y + dy[dn]
    tx = x + dx[dn]
    while 0<= tx < N and 0 <= ty < N:
        print(data[ty][tx],end="")
        ty += dy[dn]
        tx += dx[dn]
for tc in range(1, int(input())):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    jy = [N - 1, N - 1, 0]
    jx = [0, N-1, N-1]
    print("#{}".format(tc))
    for i in range(N):
        for j in range(3):
            mprint(jy[j], jx[j], j)
            print(end=" ")
            jy[j] += my[j]
            jx[j] += mx[j]
        print()