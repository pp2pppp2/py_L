import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    K = int(input())
    data = str(input())
    test = [0] * 10

    for i in range(K):
        test[int(data[i])] += 1
    card_max = 0
    card_num = 0
    for card, num in enumerate(test):
        if num > card_max:
            card_num = card
            card_max = num
        if num == card_max:
            if card > card_num:
                card_num = card

    print("#{} {} {}".format(test_case,card_num,card_max))
