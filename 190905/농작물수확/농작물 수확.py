import sys
sys.stdin = open("input.txt")

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def d(mid):
    q = [[mid, mid, 0]]
    visit[mid][mid] = 1
    result = int(m[mid][mid])
    while q:
        t = q.pop(0)
        if t[2] == mid:
            break
        for i in range(4):
            tx = t[0] + dx[i]
            ty = t[1] + dy[i]
            if 0 <= tx < N and 0 <= ty < N and visit[ty][tx] == 0:
                visit[ty][tx] = 1
                result += int(m[ty][tx])
                q.append([tx,ty,t[2]+1])
    return result
for tc in range(1, int(input())-1):
    N = int(input())
    visit = [[0 for _ in range(N)] for _ in range(N)]
    m = [input() for _ in range(N)]
    print("#{} {}" .format(tc,d(N // 2)))