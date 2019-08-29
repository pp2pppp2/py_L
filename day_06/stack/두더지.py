import sys
sys.stdin = open("input.txt")

def iswall(x,y):
    if x < 0 or y < 0 or x > N-1 or y > N-1 or visit[y][x] or not data[y][x]:
        return False
    return True

def dfs(x, y, cnt):
    if data[y][x]:
        for i in range(4):
            tx = x+dx[i]
            ty = y+dy[i]
            if iswall(tx,ty):
                cnt += 1
                visit[ty][tx] = 1
                cnt = dfs(tx,ty,cnt)
    return cnt

N = int(input())
data = [[0 for _ in range(N)] for _ in range(N)]
visit = [[0 for _ in range(N)] for _ in range(N)]

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]
for i in range(N):
    data[i] = list(map(int,input().split()))

result = []
for i in range(N):
    for j in range(N):
        cnt = 0
        cnt = dfs(j, i, cnt)
        if cnt:
            result += [cnt]
print(len(result))
result.sort(reverse=True)
for i in result:
    print(i)