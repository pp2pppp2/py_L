import sys
sys.stdin = open("input.txt")

# T = int(input())
# for tc in range(T):
#     data = [ [0 for _ in range(10)] for _ in range (10)]
#     cnt = 0
#     N = int(input())
#     for i in range(N):
#         color_in = [0] *5
#         color_in = list( map (int,input().split()))
#         for x in range (color_in[0] - 1 , color_in[2]):
#             for y in range (color_in[1] - 1 , color_in[3]):
#                 if data[x][y] != color_in[4]:
#                     data[x][y] += color_in[4]
#
#     for i in range(10):
#         for j in range(10):
#             if data[i][j] == 3:
#                 cnt += 1
#     print("#{} {}".format(tc+
T = int(input())
for tc in range(T):
    row = int(input())
    data = [[0 for _ in range(10)] for _ in range(10)]
    arr = [list(map(int, input().split())) for _ in range(row)]
    # print(arr)
    cnt = 0
    for k in range(row):
        for i in range(arr[k][0],arr[k][2]+1):
            for j in range(arr[k][1], arr[k][3]+1):
                data[i][j] += arr[k][4]
    for a in range(10):
        for b in range(10):
            if data[a][b] >= 3:
                cnt +=1
    print(data)
    print(cnt)