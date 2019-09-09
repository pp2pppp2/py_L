import sys
sys.stdin = open('그래프경로_input.txt')

def path(data, a, b):
    if result[0] == 1:
        return
    if a == b:
        result[0] = 1
        return
    for j in range(len(data)):
        if data[a][j] == 1:
            path(data, j, b)

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    data = [[0 for _ in range(V+1)] for _ in range(V+1)]

    for _ in range(E):
        i, j = map(int, input().split())
        data[i][j] = 1
    S, G = map(int, input().split())
    result = [0]
    path(data, S, G)
    print('#{} {}'.format(tc,result[0]))