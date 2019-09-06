import sys
sys.stdin = open("input.txt")

T = int(input())
data = [0] * 41000
m = [[0]*300 for _ in range(300)]
def s():
    i, j = 1, 1
    while j > 0:
        k, t = j, 1
        while k > 0:
            data[i], m[t][k] = [t, k], i
            k -= 1
            i +=1
            t +=1
            if i == 41000:
                return
        j += 1
s()
for tc in range(1,T+1):
    A, B = map(int, input().split())
    print("#{} {}".format(tc, m[data[A][0] + data[B][0]][data[A][1] + data[B][1]]))