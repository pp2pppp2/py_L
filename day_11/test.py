import sys
sys.stdin = open("input.txt")

def visited(v):
    for i in range(1, V+1):
        if ed[v][i]:
            if visit[i] == 0:
                return False
    return True

def dfs(v ,  V):
    for i in range(1 , V+1):
        if st[v][i] and visit[i] == 0 and i != v:
            if visited(i):
                visit[i] = 1
                result.append(i)
                dfs(i, V)


for tc in range(1,11):
    V , E = list(map(int,input().split()))
    node = list(map(int,input().split()))
    st = [[0 for _ in range(V + 1)] for _ in range(V + 1)]
    ed = [[0 for _ in range(V + 1)] for _ in range(V + 1)]
    visit = [0] * (V + 1)
    for i in range(0,len(node),2):
        st[node[i]][node[i+1]] += 1
        ed[node[i+1]][node[i]] += 1
    result = []
    re = []
    for i in range(1 , V + 1):
        if visited(i) and visit[i] == 0 :
            visit[i] = 1
            result.append(i)
            dfs(i, V)
    print(len(set(result)))
    print("#{} {}".format(tc, " ".join(map(str,result))))