import sys
sys.stdin = open("input.txt")

def chk():
    for i in data:
        if i == '(' or i == '{': s.append(i)
        if i == ')' or i == '}':
            if len(s) == 0: return 0
            if i == ')' and s[-1] == '{': return 0
            if i == '}' and s[-1] == '(': return 0
            s.pop()
    if len(s) == 0: return 1
    else: return 0

T = int(input())
for tc in range(1,T+1):
    data = list(input())
    s = []
    print("#{} {}" .format(tc, chk()))


