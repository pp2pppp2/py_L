import sys
sys.stdin = open("input.txt", "r")

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    K = int(input())
    data = list(map(int, input().split()))
    cnt = [0] * 101
    tmp = []
    b_cnt = 0

    for i in range(100):
        cnt[data[i]] += 1
    a = K
    b = 100
    tmp = cnt
    while a > 0:
        while not tmp[b]:
            b -= 1
        if tmp[b]:
            tmp[b] -= 1
            tmp[b-1] += 1
            a -= 1
            if not tmp[b]:
                b -= 1
    top = b
    tmp = cnt
    b = 0
    a = K
    while a > 0:
        while not tmp[b]:
            b += 1
        if tmp[b]:
            tmp[b] -= 1
            tmp[b+1] += 1
            a -= 1
            if not tmp[b]:
                b += 1
    bot = b

    print('#{} {}' .format(test_case,top-bot))
