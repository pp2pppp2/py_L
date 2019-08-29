import sys
sys.stdin = open("input.txt")

def solve():
    for K in range(21 , -1 , -1):
        for i in range(100- K + 1):
            for j in range(100- K + 1):
                if j + K < 101:
                    for k in range(K // 2):
                        if data[i][j+k] != data[i][j+K - 1 - k]:
                            break
                        if k == (K//2)-1:
                            return K
                if i + K < 101:
                    for k in range(K//2):
                        if data[i+k][j] != data[i + K - 1 - k][j]:
                            break
                        if k == (K//2)-1:
                            return K

T = 10
for tc in range(T):
    t = int(input())
    data = [ [0 for _ in range(100)] for _ in range(100)]

    for i in range(100):
        data[i] = list(input())
    result = solve()

    print("#{} {}".format(tc+1, result))