import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1,T+1):
    data = input()
    s = []
    for i in data:
        if s == []: s += i
        elif s[-1] == i: s.pop()
        elif s[-1] != i: s += i
    print("#{} {}" .format(tc,len(s)))