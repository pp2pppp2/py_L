import sys
sys.stdin = open("input.txt")

def solve(N,M):
    result =''
    for i in range(N):
        for j in range(N):
            if j + M < N+1:
                cnt = 0
                for k in range(M // 2):
                    if data[i][j+k] == data[i][j+M - 1 - k]:
                        cnt +=1
                    if cnt == M//2:
                        result = data[i][j:j+M]
                        return "".join(result)
            if i + M < N+1:
                cnt = 0
                for k in range(M//2):
                    if data[i+k][j] == data[i + M - 1 - k][j]:
                        cnt +=1
                    if cnt == M//2:
                        for a in range(M):
                            result += data[i+a][j]
                        return result

T = int(input())

for tc in range(T):
    result = 0
    N, M = map(int,input().split())
    data = [ [0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        data[i] = list(input())

    result = solve(N,M)

    print("#{} {}".format(tc+1, result))