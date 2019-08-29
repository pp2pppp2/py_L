import sys
sys.stdin = open("input.txt")
def iswall(d_c):
    tem_x = x + dx[d_c]
    tem_

T = int(input())
for tc in range(1,T+1):
    K = int(input())
    data = [[0 for _ in range(K)] for _ in range(K)]
    x = y = 0
    a = 0
    d_c = 0
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    while a < K ** 2:
        a += 1
        data[y][x] = a
        iswall(d_c)
        x += dx[d_c]
        y += dy[d_c]



    print("#{}" .format(tc))
    for i in range(K):
        for j in range(K):
            print(data[i][j], end=" ")
        print()
