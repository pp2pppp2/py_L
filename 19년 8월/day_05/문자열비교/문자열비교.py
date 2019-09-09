import sys
sys.stdin = open("input.txt")

def solve():
    for i in range(len(te)-1, len(pa)-2, -1):
        if te[i] == pa[-1]:
            for j in range(1,len(pa)):
                if te[i-j] != pa[-j-1]:
                    break
                if j == len(pa)-1:
                    return 1
    return 0

T = int(input())
for tc in range(1,T+1):
    pa = [0]*100
    te = [0]*1000
    pa = list(input())
    te = list(input())
    result = solve()

    print("#{} {}".format(tc, result))


