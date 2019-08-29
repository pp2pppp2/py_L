import sys
sys.stdin = open("input.txt", "r")

def v(s):
    for i in data:
        if i in o:
            if i == '+' and len(s) > 1: s += [s.pop() + s.pop()]
            elif i == '*' and len(s) > 1: s += [s.pop() * s.pop()]
            elif i == '-' and len(s) > 1:
                a = s.pop()
                s += [s.pop() - a]
            elif i == '/' and len(s) > 1:
                a = s.pop()
                s += [s.pop() // a]
            else:
                return 'error'
        elif i == '.':
            if len(s) == 1:
                return s.pop()
            return 'error'
        else:
            s += [int(i)]
T = int(input())
for tc in range(1,T+1):
    data = list(input().split())
    s = []
    o = '+-/*'
    result = v(s)
    print("#{} {}".format(tc, result))