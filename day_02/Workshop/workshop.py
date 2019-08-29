import sys
sys.stdin = open("input.txt")

data = [[0 for _ in range(100)] for _ in range(100)]

T = 10
for tc in range(1,T+1):
    input()
    for i in range(100):
        data[i] = list(map(int,input().split()))
    max_tmp = 0
    for i in range(100):
        col_sum = 0
        row_sum = 0
        for j in range (100):
            col_sum += data[j][i]
            row_sum += data[i][j]
        if max_tmp < col_sum:
            max_tmp = col_sum
        if max_tmp < row_sum:
            max_tmp = row_sum

    col_sum = 0
    row_sum = 0
    for i in range (100):
        col_sum += data[i][i]
        row_sum += data[99-i][i]
    if max_tmp < col_sum:
        max_tmp = col_sum
    if max_tmp < row_sum:
        max_tmp = row_sum

    print("#{} {}".format(tc,max_tmp))