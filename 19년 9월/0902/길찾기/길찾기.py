import sys
sys.stdin = open("input.txt")


def s(a):
    global result
    visit[a] = 1
    if a == 99:
        result = 1
    for i in range(100):
        if n[a][i] == 1 and visit[i] == 0:
            s(i)
    visit[a] = 0


for tc in range(1,11):
    T , K = map(int,input().split())
    data = [0] * K * 2
    data = list(map(int,input().split()))
    visit = [0] * 100
    n = [[0 for _ in range(100)] for _ in range(100)]
    for i in range(0, K*2 , 2):
        n[data[i]][data[i+1]] = 1
    result = 0
    s(0)
    print("#{} {}" .format(tc,result))