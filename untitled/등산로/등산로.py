# import sys
# sys.stdin = open("rinput.txt")
#
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]
# def d(y, x, flag, cnt , xh):
#     global N, ret
#     if cnt > ret:
#         ret = cnt
#     for i in range(4):
#         tx = x + dx[i]
#         ty = y + dy[i]
#         if 0 <= tx < N and 0 <= ty < N and visit[ty][tx] == 0:
#             if flag == 0:
#                 if m[y][x] > m[ty][tx] - K:
#                     visit[ty][tx] = 1
#                     d(ty, tx, 1, cnt+1, m[y][x] - 1)
#                     visit[ty][tx] = 0
#                 if m[y][x] > m[ty][tx]:
#                     visit[ty][tx] = 1
#                     d(ty, tx, 0, cnt+1, m[y][x])
#                     visit[ty][tx] = 0
#             else:
#                 if m[y][x] > m[ty][tx] and xh > m[ty][tx]:
#                     visit[ty][tx] = 1
#                     d(ty, tx, 1, cnt+1, m[y][x])
#                     visit[ty][tx] = 0
# for tc in range(int(input())):
#     N, K = map(int, input().split())
#     m = [list(map(int, input().split())) for _ in range(N)]
#     visit = [[0 for _ in range(N)] for _ in range(N)]
#     mx = 0
#     st = []
#     ret = 0
#     for y in range(N):
#         for x in range(N):
#             if m[y][x] > mx:
#                 mx = m[y][x]
#                 st = [[y, x]]
#             elif m[y][x] == mx:
#                 st.append([y, x])
#     for i in st:
#         visit[i[0]][i[1]] = 1
#         d(i[0], i[1], 0, 1, 30)
#         visit[i[0]][i[1]] = 0
#     print('#{} {}' .format(tc+1, ret))

a = [[0,0,0,0,0,0,0,0,0,0],

[0,0,0,0,0,0,0,0,0,0],

[0,0,0,0,0,0,0,0,0,0],

[0,0,0,0,0,0,0,0,0,0],

[0,0,0,0,0,0,4,0,0,0],

[0,0,0,0,0,4,4,0,0,0],

[0,0,0,0,3,0,4,0,0,0],

[0,0,0,2,3,0,0,0,5,5],

[1,2,2,2,3,3,0,0,0,5],

[1,1,1,0,0,0,0,0,0,5]]

for i in a:
    for j in i:
        print(j, end=" ")
    print()