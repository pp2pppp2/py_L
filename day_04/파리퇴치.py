import sys
sys.stdin = open("파리.txt")

T = int(input())
data = [ [0 for _ in range(15)] for _ in range(15)]

for tc in range(T):
    result = 0
    N, K = map(int, input().split())
    for i in range(N):
        data[i] = list(map(int,input().split()))
    for i in range(N - (K-1)):
        for j in range(N - (K-1)):
            result_tmp = 0
            for a in range(K):
                for b in range(K):
                    result_tmp += data[i+a][j+b]
            if result < result_tmp:
                result = result_tmp
    print("#{} {}".format(tc+1, result))