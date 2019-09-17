arr = [1, 2, 4, 7, 8, 3]
arr = [6, 6, 7, 7, 6, 7]
arr = [0, 5, 4, 0, 6, 0]
# arr = [1, 0, 1, 1, 2, 3]
tr = []
visit =[0] * 6

def baby(tr):
    global flag
    if tr[0] == tr[1] == tr[2] or tr[0] == tr[1] - 1 == tr[2] - 2:
        if tr[3] == tr[4] == tr[5] or tr[3] == tr[4] - 1 == tr[5] - 2:
            flag = 1

def d(dep):
    global tr
    if dep == 6:
        baby(tr)
        return
    if flag == 1:
        return
    for i in range(6):
        if visit[i] == 0:
            visit[i] = 1
            tr += [arr[i]]
            d(dep + 1)
            tr.pop()
            visit[i] = 0
flag = 0
d(0)
if flag:
    print('bg')
else:
    print('no')