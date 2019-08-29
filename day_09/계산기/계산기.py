import sys
sys.stdin = open("input.txt")
for tc in range(1,11):
    N = int(input())
    data = list(input())
    s = []
    aa = ["(", "+", "*", ")"]
    result = []
    for i in data:
        if i in aa:
            if i == aa[0]: s += [i]
            elif i == aa[1]:
                if s[-1] == '*' or s[-1] == '+':
                    result += [s.pop()]
                    s += [i]
                else: s += [i]
            elif i == aa[2]:
                if s[-1] == '*':
                    result += [s.pop()]
                    s += [i]
                else: s += [i]
            else:
                while (s[-1] != '('): result += [s.pop()]
                s.pop()
        else: result += [i]

    for i in result:
        if i in aa:
            if i == '+': s += [s.pop() + s.pop()]
            else: s += [s.pop() * s.pop()]
        else: s += [int(i)]
    print("#{} {}".format(tc, s[0]))