



n = len(arr)
for i in range(1 << n):
    tmp = 0
    tmp_lt= []
    for j in range(n):
        if i & (1 << j):
            tmp += arr[j]
            tmp_lt += [arr[j]]
    if tmp == 10:
        print("존재")
        print(tmp_lt)