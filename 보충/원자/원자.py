import sys
sys.stdin = open("input.txt")

def ck2():
   tmp = []
   C = []
   for i in range(allen):
       tx, ty = al[i][0] + dr[al[i][2]][0], al[i][1] + dr[al[i][2]][1]
       if (tx, ty) not in tmp:
           tmp.append((tx, ty))
       else:
           if (tx, ty) not in C:
               C.append((tx, ty))
   while C:
       dela(*C.pop())
def dela(x, y):
   global E, allen
   tmp = []
   for i in range(allen):
       if al[i][0] + dr[al[i][2]][0] == x and al[i][1] + dr[al[i][2]][1] == y:
           E += al[i][3]
           tmp.append(i)
   for tm in tmp[::-1]:
       allen -= 1
       al[tm], al[allen] = al[allen], al[tm]
def moa():
   global allen
   tmp = []
   for i in range(allen):
       al[i][0] += dr[al[i][2]][0]
       al[i][1] += dr[al[i][2]][1]
       if not (-2000 <= al[i][0] <= 2000 and -2000 <= al[i][1] <= 2000):
           tmp.append(i)
   for tm in tmp[::-1]:
       allen -= 1
       al[tm], al[allen] = al[allen], al[tm]

dr = [[0, 1], [0, -1], [-1, 0], [1, 0]]
T = int(input())
for t in range(1, T + 1):
   N = int(input())
   al = [list(map(int, input().split())) for _ in range(N)]
   for A in al:
       A[0] = A[0]*2
       A[1] = A[1]*2
   E = 0
   allen = len(al)
   while allen > 1:
       ck2()
       moa()
   print('#{} {}'.format(t, E))