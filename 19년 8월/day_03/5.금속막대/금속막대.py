import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(T):
    N = int(input())
    data_r = [[0,0] for _ in range(N)]
    data = list(map(int,input().split()))
    for i in range(N):
        data_r[i] = [data[i*2] , data[i*2 + 1]]

    for a in range(N):
        result = []
        result = [data_r[a]]
        for i in range(N-1):
            for j in range(N):
                if result[-1][1] == data_r[j][0]:
                    result += [data_r[j]]
        if (len(result) == N):
            break

    print("#{}" .format(tc+1), end=" ")
    for i in range(N):
        for j in range(2):
            print(result[i][j], end=" ")
    print()