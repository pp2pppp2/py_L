import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    data = list(map(int, input().split()))
    bus_stop = list(map(int, input().split()))

    map_bus = [0] * (data[1]+1)
    for i in bus_stop:
        map_bus[i] += 1
    a = data[0]
    result = 0
    cnt = 0
    while a < data[1]:
        if a == 0:
            cnt = 0
            break
        if map_bus[a] == 1:
            map_bus[a] -= 1
            a += data[0]
            cnt += 1
        else:
            a -= 1

    print("#{} {}".format(test_case, cnt))
