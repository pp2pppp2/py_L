import sys
sys.stdin = open("input.txt")

f = '+-*/'
def d(a):
    if a:
        n1 = d(no[a][1])
        n2 = d(no[a][2])
        if no[a][0] not in f:
            return int(no[a][0])
        else:
            if no[a][0] == '+':
                return n1 + n2
            if no[a][0] == '-':
                return n1 - n2
            if no[a][0] == '*':
                return n1 * n2
            if no[a][0] == '/':
                return n1 / n2
for tc in range(1,11):
    N = int(input())
    nod = [0] * 3
    no = [[0 for _ in range(3)] for _ in range(N+1)]
    for i in range(1, N+1):
        nod = list(input().split())
        if nod[1] in f:
            no[i][0] = nod[1]
            no[i][1] = int(nod[2])
            no[i][2] = int(nod[3])
        else:
            no[i][0] = nod[1]
    print("#{} {}".format(tc, int(d(1))))

