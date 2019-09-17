N = 10
A = [0 for _ in range(N)]
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def printSet(n, sum):
    if sum == 10:
        for i in range(n):
            if A[i]:
                print("%d " % data[i], end="")
        print()
def powerset(n, k, sum):
    if n == k:
        printSet(n, sum)
    else:
        A[k] = 1
        powerset(n, k+1, sum + data[k])
        A[k] = 0
        powerset(n, k + 1, sum)

powerset(N, 0, 0)