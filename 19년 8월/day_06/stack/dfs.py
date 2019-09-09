#7 8
#1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
import sys
sys.stdin = open("input.txt")

def dfs(v):
    visit[v] = 1
    print(v , end= " ")
    for i in range(N+1):
        if rd[v][i] and not visit[i]:
            dfs(i)


N,K = map(int,input().split())
data= list(map(int,input().split()))
visit = [0] * 8
rd = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(0,len(data),2):
    rd[data[i]][data[i+1]] += 1
    rd[data[i+1]][data[i]] += 1
for i in range(N+1):
    print("{} {}".format(i, rd[i]))

dfs(1)
