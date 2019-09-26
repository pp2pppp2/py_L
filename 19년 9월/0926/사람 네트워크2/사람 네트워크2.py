import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    data = list(map(int, input().split()))
    nod = [[0 for _ in range(data[0])] for _ in range(data[0])]
    k = 1
    for y in range(data[0]):
        for x in range(data[0]):
            if y == x: k += 1; continue
            if data[k] == 0:
                nod[y][x] = 987654321
            else:
                nod[y][x] = data[k]
            k += 1

    for k in range(data[0]):
        for i in range(data[0]):
            if i == k: continue
            for j in range(data[0]):
                if j == k or j == i: continue
                nod[i][j] = min(nod[i][k] + nod[k][j], nod[i][j])
    ret = 987654321
    for i in range(data[0]):
        ret = min(sum(nod[i]), ret)
    print("#{} {}".format(tc, ret))