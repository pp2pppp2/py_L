import sys
sys.stdin = open("input.txt")

# T = 10
#
# for tc in range(T):
#     result = 0
#     K = int(input())
#     data = [ [0 for _ in range(8)] for _ in range(8)]
#
#     for i in range(8):
#         data[i] = list(input())
#
#     for i in range(8):
#         for j in range(8):
#             if j + K < 9:
#                 cnt = 0
#                 for k in range(K // 2):
#                     if data[i][j+k] == data[i][j+K - 1 - k]:
#                         cnt +=1
#                     if cnt == K//2:
#                         result += 1
#             if i + K < 9:
#                 cnt = 0
#                 for k in range(K//2):
#                     if data[i+k][j] == data[i + K - 1 - k][j]:
#                         cnt +=1
#                     if cnt == K//2:
#                         result += 1
#     print("#{} {}".format(tc+1, result))
for tc in range(10):
    data = [[0 for _ in range(8)] for _ in range(8)]
    word = int(input())
    cnt1 = 0
    cnt2 = 0
    for i in range(8):
        data[i] = list(input())
        for x in range(9-word):
            if data[i][x] == data[i][word-x-1] and data[i][x+1] == data[i][word-x-2]:
                cnt1 += 1
    for i in range(9-word):
        for y in range(8):
            if data[i][y] == data[i+word-1][y] and data[i+1][y] == data[i+word-2][y]:
                cnt2 +=1
    print(cnt1)
    print(cnt2)