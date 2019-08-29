import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1,T+1):
    pa = list(input())
    te = list(input())
    data = [0] * 100
    for i in range(len(pa)):
        data[ord(pa[i])] = 1

    for i in range(len(te)):
        if data[ord(te[i])]:
            data[ord(te[i])] +=1

    print ("#{} {}".format(tc,max(data)-1))