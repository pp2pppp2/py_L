da = '01D06079861D79F99F'
re = ''
da = list(da)
out = ''
for i in da:
    if '0' <= i <= '9':
        tmp = int(i)
    else:
        tmp = ord(i) - ord('A') + 10
    for j in range(3, -1, -1):
        out += '1' if tmp & (1 << j) else '0'

for i in range(11):
    n = 0
    for k in range(i*7, i*7+7, 1):
        if k < 72:
            n = n * 2 + int(out[k])
        else:
            break
    print(n, end=" ")