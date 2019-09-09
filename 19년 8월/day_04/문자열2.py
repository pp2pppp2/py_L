def atoi(string):
    value = 0
    i = 0
    while( i < len(string)):
        c = string[i]
        if c >= '0' and c <= '9':
            digit = ord(c) - ord('0')
        else:
            break
        value = (value * 10) + digit;
        i += 1
    return value

def itoa(x):
    value = []
    while (x):
        c = x % 10
        value += [chr(c+48)]
        x = x // 10
    return "".join(reversed(value))

a = 123
print(type(a))
b = itoa(a)
print(b)
c = int(a)
print(type(c))