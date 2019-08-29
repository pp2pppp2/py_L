def PrintArr(n,cnt):
    for i in range(n):
        print(arr[i], end=" ")
    print()
def perm(n,k,cnt):
    if k == n:
        PrintArr(n, cnt)
    else:
        for i in range(k, n):
            arr[k],arr[i] = arr[i], arr[k]
            perm(n, k+1, cnt)
            arr[k], arr[i] = arr[i], arr[k]
arr = [4,3,2,1]
perm(4,0,3)

