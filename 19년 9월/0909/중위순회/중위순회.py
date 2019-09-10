import sys
sys.stdin = open("input.txt")

def d(a):
    if int(a) != 0:
        d(nod[int(a)][1])
        print(nod[int(a)][0], end="")
        d(nod[int(a)][2])
for tc in range(1, 11):
    N = int(input())
    nod = [[0 for _ in range(4)] for _ in range(N+2)]
    for i in range(1, N+1):
        tmp = list(input().split())
        for j in range(len(tmp)-1):
            nod[i][j] = tmp[j+1]
    print("#{}".format(tc), end=" ")
    d(1)
    print()
