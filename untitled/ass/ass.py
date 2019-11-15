a = ['(', ')']
cc = 5
num = [cc, cc]
b = []
s = []
st = []
cnt = 0

def ch():
    global cnt
    for z in b:
        if z == '(':
            s.append('(')
        if z == ')':
            if s == []:
                return False
            s.pop(-1)
    return True

def d():
    global cnt
    if len(b) == 2*cc:
        if ch():
            print(b)
            cnt += 1
        return

    for i in range(2):
        if num[i] != 0:
            num[i] -= 1
            b.append(a[i])
            d()
            b.pop()
            num[i] += 1

d()
print(cnt)