import sys
sys.stdin = open('input.txt')

h = [0] * 62
tmp = [25, 19, 61, 35, 49, 47, 59, 55, 11]
for i in range(9):
    h[tmp[i]] = i+1
def ct(data):
    global result,ret
    out = ''
    for i in data:
        if '0' <= i <= '9':
            vvv = int(i)
        else:
            vvv = ord(i) - ord('A') + 10
        for j in range(3, -1, -1):
            out += '1' if vvv & (1 << j) else '0'
    k = len(out)
    st = 0
    t = 0
    while k:
        k -= 1
        result = []
        if out[k] == '1':
            if st == 0:
                st = k
            if t % 2 == 0:
                t += 1
        if out[k] == '0' and t % 2 == 1:
            t += 1
        if t == 5:
            leng = st - k
            t = 0
            for g in range(8):
                dum = 0
                j = 0
                for i in range(7*g*leng//7, 7*g*leng//7 + leng, leng//7):
                    dum += int(out[st - i]) * 2 ** j
                    j += 1
                result += [dum]
            result.reverse()
            if not asdg.get(str(result)):
                asdg[str(result)] = 1
                gg = 0
                for i in range(8):
                    gg += h[result[i]]
                    if i % 2 == 0:
                        gg += h[result[i]] * 2
                    result[i] = h[result[i]]
                if gg % 10 == 0 :
                    ret += sum(result)
            k = st - leng*8
            st = 0
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    result = []
    ret = 0
    asdg = {}
    ss = set()
    dat = ''
    for i in range(N):
        dat = input().strip()
        ss.add(dat)
    for j in range(len(ss)):
        d = ss.pop()
        ct(d)
    print("#{} {}".format(tc, ret))