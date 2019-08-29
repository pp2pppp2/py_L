count = 0
N = 10
total = 0
A = [0 for _ in range(N)]
data = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

def printSet(n):
    global count
    tmp = 0
    tp = []
    for i in range(n):
        if A[i] == 1:
            tmp += data[i]
            tp += [data[i]]
    if tmp == 10:
        print(tp)

def powerset(n, k, sum):
    global total
    if n == k:
        printSet(n)
    else:
        if sum > 10:
            return
        total += 1
        A[k] = 1
        powerset(n,k+1, sum + data[k])
        A[k] = 0
        powerset(n,k+1, sum)

powerset(N,0,0)
print(total)