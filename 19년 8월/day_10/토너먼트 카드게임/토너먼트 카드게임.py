import sys
sys.stdin = open("input.txt")

def g(a , b):
    if data[a] == 1 and data[b] == 2 or  data[a] == 2 and data[b] == 3 or data[a] == 3 and data[b] == 1: return b
    # if ( data[a] + 1 ) % 3 == data [b] : return b
    return a

def s(l ,r):
    if l - r == 0: return l
    return g(s(l , (l + r) // 2) , s((l + r)//2 + 1 , r))

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = list(map(int,input().split()))
    print ("#{} {}".format(tc,s(0, len(data)-1)+1))