import sys
sys.stdin = open("input.txt")
Q = [[0 for _ in range(10)] for _ in range(10)]
for tc in range(1, int(input())+1):
    print("#{}" .format(tc))
    for y in range(int(input())):
        for x in range(y + 1):
            if x == 0 or x == y:
                Q[y][x] = 1
            else:
                Q[y][x] = Q[y - 1][x] + Q[y - 1][x - 1]
            print(Q[y][x], end=" ")
        print()