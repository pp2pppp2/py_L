import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    data = [[99 for _ in range(15)] for _ in range(5)]
    for i in range(5):
        data[i] = list(input())
        while len(data[i]) < 15:
            data[i].append(99)
    print("#{} ".format(tc), end="")
    for i in range(15):
        for j in range(5):
            if data[j][i] != 99:
                print(data[j][i], end="")
    print()