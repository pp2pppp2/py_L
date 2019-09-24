import sys
sys.stdin = open("input.txt")

# def isuni(a, b, vs):
#     for i in range(V+1):
#         if uni[a][i] == 1 and vs[i] == 0:
#             if i == b:
#                 return False
#             vs[i] = 1
#             if not isuni(i, b, vs):
#                 return False
#     return True
#
# def mst():
#     ret = 0
#     cnt = 0
#     for i in range(E):
#         vs = [0] * (V+1)
#         if isuni(nod[i][0], nod[i][1], vs):
#             ret += nod[i][2]
#             uni[nod[i][0]][nod[i][1]] = 1
#             uni[nod[i][1]][nod[i][0]] = 1
#             cnt += 1
#         if cnt == V:
#             break
#     return ret
#
# T = int(input())
# for tc in range(1, T+1):
#     V, E = map(int, input().split())
#     uni = [[0] * (V+1) for _ in range(V+1)]
#     nod = [0] * E
#     for i in range(E):
#         n1, n2, w = map(int, input().split())
#         nod[i] = [n1, n2, w]
#     nod.sort(key=lambda x: x[2])
#     print("#{} {}".format(tc, mst()))
def findSet(x):
    if x == p[x]: return x
    else: return findSet(p[x])

def mst():
    global V
    cnt = 0
    total = 0
    i = 0
    while cnt < V:
        p1 = findSet(edge[i][0])
        p2 = findSet(edge[i][1])
        if p1 != p2:
            total += edge[i][2]
            cnt += 1
            p[p2] = p1
        i += 1
    return total

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    edge = [list(map(int, input().split()))]
    edge.sort(key=lambda x: x[2])
    p = list(range(V+1))
    print(mst())

