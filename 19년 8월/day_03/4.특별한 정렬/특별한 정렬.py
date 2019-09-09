import sys
sys.stdin = open("input.txt")

def selectionSort(a):
    for i in range(0, len(a)-1):
        min_1 = i
        max_1 = i
        for j in range(i+1, len(a)):
            if a[min_1] > a[j]:
                min_1 = j
            if a[max_1] < a[j]:
                max_1 = j
        if i % 2 == 0:
            a[i], a[max_1] = a[max_1], a[i]
        else:
            a[i], a[min_1] = a[min_1], a[i]

T = int(input())
for tc in range(T):
    K = int(input())
    tmp = [0] * K
    tmp = list(map(int, input().split()))
    selectionSort(tmp)
    print("#{}" .format(tc+1) ,end = " ")
    for i in range(10):
        print("{}" .format(tmp[i]) , end=" ")
    print()