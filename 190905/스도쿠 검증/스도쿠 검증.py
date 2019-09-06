import sys
sys.stdin = open("input.txt")

def d():
    for y in range(9):
        c,r= 0,0
        for x in range(9):
            c += m[y][x]
            r += m[x][y]
            if y % 3 == 0 and x % 3 == 0:
                t = 0
                for ty in range(y, y+3):
                    for tx in range(x, x+3):
                        t+=m[ty][tx]
                if t != 45:return 0
        if c != 45 or r != 45:return 0
    return 1
for tc in range(1,int(input())+1):
    m = [list(map(int,input().split())) for _ in range(9)]
    print("#{} {}" .format(tc, d()))
