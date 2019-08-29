import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    K = list(map(int, input().split()))
    data = list(map(int, input().split()))
    res_max = sum(data[0:K[1]])
    res_min = sum(data[0:K[1]])

    for i in range(0,len(data)-K[1]+1):
        a = sum(data[i:i+K[1]])
        if a > res_max:
            res_max = a
        if a < res_min:
            res_min = a
    print("#{} {}".format(test_case, res_max - res_min))
