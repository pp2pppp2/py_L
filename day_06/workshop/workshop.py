import sys
sys.stdin = open("input.txt")

dx = [1, -1 ,0]
dy = [0, 0, -1]
def iswall(x,y):
    if x < 0 or x > 99 or not data[y][x] or visit[y][x]:
        return False
    return True

def dfs(x,y):
    if y == 0:
        return x
    visit[y][x] = 1
    if data[y][x]:
        for i in range(3):
            tx = x+dx[i]
            ty = y+dy[i]
            if iswall(tx, ty):
                result = dfs(tx,ty)
                if result:
                    return result
    visit[y][x] = 0
    return result

for tc in range(1,11):
    T = int(input())
    data = [[0 for _ in range(100)] for _ in range(100)]
    visit = [[0 for _ in range(100)] for _ in range(100)]

    for i in range(100):
        data[i] = list(map(int,input().split()))

    a= 0
    for i in range(100):
        if data[99][i] == 2:
            a=dfs(i,99)
            print("#{} {}".format(tc,a))