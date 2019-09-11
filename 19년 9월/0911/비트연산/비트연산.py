dat = '0000000111100000011000000111100110000110000111100111100111111001100111'
dat = list(dat)
tmp, k= 0, 0
data = ''
k = 0
for i in range(69 , -1 , -1):
    tmp += int(dat[i]) * (2 ** k)
    k += 1
    if i % 7 == 0:
        print(tmp, end=" ")
        k = 0
        tmp = 0

for i in range(10):
    n = 0
    for j in range(i*7, i*7+7, 1):
        n = n*2 + int(dat[j])
    print(n, end=" ")
print()