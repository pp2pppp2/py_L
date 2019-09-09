def bfs(G , v):
    visited = [0] * 7
    que = []
    que.append(v)
    while len(que):
        t = que.pop(0)
        if not visited[t]:
            visited[t] = 1
            print(t)
        for i in G[t]:
            if i and visited[i] == 0 :
                que.append(i)


G = [[0 for _ in range(8)] for _ in range(8)]
d = [1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7]
for i in range(0,len(d),2):
    G[d[i]][d[i+1]] = 1
    G[d[i+1]][d[i]] = 1
print(G)
bfs(G, 1)
