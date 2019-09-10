def dd(a):
    if a != 0:
        print(a, end=" ")
        dd(g[a][0])
        dd(g[a][1])
    return
nod = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'
nod = list(map(int,nod.split()))

g = [[0 for _ in range(2)] for _ in range(14)]

for i in range(0, len(nod), 2):
    if g[nod[i]][0] != 0:
        g[nod[i]][1] = nod[i+1]
    else:
        g[nod[i]][0] = nod[i+1]
dd(1)


V, E = map(int, input().split())
tree = [[0 for _ in range(3)] for _ in range(V+1)]
tmp = list(map(int, input().split()))

for i in range(E):
    n1 = tmp[i*2]
    n2 = tmp[i*2+1]
    if not tree[n1][0]:
        tree[n1][0] = n2
    else:
        tree[n1][1] = n2

print(tree)