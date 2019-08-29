def bruteforce(text, pattern):
    i = 0
    j = 0
    while j < len(pattern) and i < len(text):
        if text[i] != pattern[j] :
            i = i -j
            j = -1
        i = i+1
        j = j+1
    if j == len(pattern) : return i - len(pattern)
    else : return -1
def bruteforce2(text, pattern):
    for i in range(len(text)-len(pattern)+1):
        cnt = 0
        for j in range(len(pattern)):
            if text[i+j] != pattern[j]:
                break
            else: cnt +=1
        if(cnt >= len(pattern)) : return i
    return -1
text = "TTTTAACCA"
pattern = "AC"
print("{}".format(bruteforce2(text,pattern)))