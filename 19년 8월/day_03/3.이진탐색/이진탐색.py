import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(T):
    data = [0] * 3
    data = list( map(int , input().split()))
    start = [1,1]
    end = [data[0], data[0]]
    middle = [0, 0]
    result = ''
    while result == '':
        middle[0] = (start[0] + end[0]) // 2
        middle[1] = (start[1] + end[1]) // 2
        if middle[0] == data[1]:
            result += 'A'
        elif middle[0] > data[1]:
            end[0] = middle[0]
        else:
            start[0] = middle[0]

        if middle[1] == data[2]:
            result += 'B'
        elif middle[1] > data[2]:
            end[1] = middle[1]
        else:
            start[1] = middle[1]

    if result == 'AB':
        result = 0

    print("#{} {}" .format(tc+1,result))
