'''
()()((()))
((()((((()()((()())((())))))
'''
s = list()

def check_ma(data):
    for i in data:
        if i == '(': s.append(i)
        elif i == ')':
            if len(s): s.pop()
            else: return False
    if len(s): return False
    return True

data = '((()((((()()((()())((())))))'
print(check_ma(data))
