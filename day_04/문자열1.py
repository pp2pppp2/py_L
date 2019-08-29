def my_strrev_1(ary):
    data = []
    for i in reversed(ary):
        data += i
    return "".join(data)

def my_strrev(ary):
    str = list(ary)
    for i in range(len(str)//2):
        str[i] , str[len(ary)-1-i] = str[len(ary)-1-i] , str[i]
        # t = ary[i]
        # str[i] = str[len(str)-1-i]
        # str[len(ary) - 1 - i ] = t
    return "".join(str)
ary = 'abcde'
ary = my_strrev(ary)
# ary = my_strrev(ary)
print(ary)