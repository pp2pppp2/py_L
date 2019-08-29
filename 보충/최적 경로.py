import sys
sys.stdin = open("input.txt")

def dfs(K, cnt , x):
    if cnt == K:
        tmp[0] = 0
        tmp_ls.append(com)
        for i in range(K):
            tmp[0] += abs(tmp_ls[i][0]-tmp_ls[i+1][0]) + abs(tmp_ls[i][1] - tmp_ls[i+1][1])
        if mr[0] > tmp[0]:
            mr[0] = tmp[0]
        tmp_ls.pop()
        return
    for i in range(K):
        if not visit[i]:
            tmp_ls.append([data[i-1][0], data[i-1][1]])
            visit[i] = 1
            dfs(K,cnt+1,i)
            visit[i] = 0
            tmp_ls.pop()

T = int(input())
for tc in range(1,T+1):
    K = int(input())
    data_in = list(map(int,input().split()))
    visit= [0] * K
    com = [data_in[0] , data_in[1]]
    home = [data_in[2],data_in[3]]
    data =[[0, 0] for _ in range(K)]
    c = 0
    for i in range(4 ,len(data_in) , 2):
        data[c][0] = data_in[i]
        data[c][1] = data_in[i+1]
        c += 1
    print(data)
    cnt = 0
    mr = [999999]
    tmp = [0]
    tmp_bf = [0,0]
    tmp_ls =[[data_in[2],data_in[3]]]
    dfs(K,cnt,0)
    print(mr[0])
