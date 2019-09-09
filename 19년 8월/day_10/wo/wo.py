import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int,input().split())
    data = [[0 for _ in range(M)] for _ in range(N)]
    t = [list(map(int,input().split())) for _ in range(K)]
    d = [0 for _ in range(11)]
    d[0] = N * M
    for a in range(K):
        cnt = 0
        for i in range(2):
            for y in range(t[a][0] , t[a][2] + 1):
                for x in range(t[a][1], t[a][3] + 1):
                    if data[y][x] > t[a][4]:
                        cnt = 1
                    if i == 1 and cnt == 0 and data[y][x] < t[a][4]:
                        d[data[y][x]] -= 1
                        d[t[a][4]] += 1
                        data[y][x] = t[a][4]

    print("#{} {}" .format(tc,max(d)))