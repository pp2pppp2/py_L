import sys
sys.stdin = open("input.txt", "r")

def iswall(x,y):
    if x < 0 or x >= 5 : return True
    if y < 0 or y >= 5 : return True
    return False

def calabs(x,y):
    if x - y > 0: return x - y
    else: return y - x

data = [[0 for _ in range(5)] for _ in range(5)]
for i in range(5):
    data[i] = list(map(int,input().split()))


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

sum = 0
for x in range(len(data)):
    for y in range(len(data[x])):
        for i in range(4):
            testX = x + dx[i]
            testY = y + dy[i]
            if iswall(testX,testY) == False:
                sum += calabs(data[x][y], data[testX][testY])

print("sum = {}" .format(sum))