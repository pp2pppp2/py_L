def h(t):
    if t == 1:
        return 1
    else:
        return t + h(t-1)
print(h(10))
