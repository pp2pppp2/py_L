import sys
sys.stdin = open("input.txt")

T=int(input())
for tc in range(1,T+1):
    t,c = input().split()
    data = list(input().split())
    dic = {}
    for i in data:
        if dic.get(i):
            dic[i] += 1
        else:
            dic[i] = 1
    print("#{}".format(tc), end=" ")
    result = ['ZRO', 'ONE','TWO','THR','FOR','FIV','SIX','SVN','EGT','NIN']
    for i in result:
        for j in range(dic.get(i)):
            print(i, end=" ")
    print()
