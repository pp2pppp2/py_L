import sys
sys.stdin = open("input.txt")

dy =[0, 0, 1, -1]
dx =[1, -1, 0, 0]

def d(x, y):
    data[y][x] = 1
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if data[ty][tx] == 0:
            d(tx,ty)
        if data[ty][tx] == 3:
            result[0] = 1

for tc in range(1,11):
    T = int(input())
    data = [[0 for _ in range(16)] for _ in range(16)]

    for i in range(16):
        data[i] = list(map(int,input()))

    result = [0]
    for i in range(16):
        for j in range (16):
            if data[i][j] == 2:
                d(j, i)

    print("#{} {}" .format(tc,result[0]))