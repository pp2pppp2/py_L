import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    K = int(input())
    data = list(map(int, input().split()))
    res_max = data[0]
    res_min = data[0]
    for i in data:
        if i > res_max:
            res_max = i
        if i < res_min:
            res_min = i
    print("#{} {}".format(test_case, res_max - res_min))
