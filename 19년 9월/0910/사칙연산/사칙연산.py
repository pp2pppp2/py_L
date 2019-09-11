import sys
sys.stdin = open("input.txt")

f = '+-*/'
def d(a):
    if no[a][0] in f:
        n1,n2 = d(no[a][1]), d(no[a][2])
        return str(int(eval(n1+no[a][0]+n2)))
    else:
        return no[a][0]
for tc in range(1,11):
    N = int(input())
    nod = [0]*3
    no = [[0]*3 for _ in range(N+1)]
    for i in range(1, N+1):
        nod = list(input().split())
        no[i][0] = nod[1]
        if nod[1] in f:
            no[i][1] = int(nod[2])
            no[i][2] = int(nod[3])
    print("#{} {}".format(tc, int(d(1))))

