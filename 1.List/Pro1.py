import sys
sys.stdin = open("input.txt")
T = 10
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    sr = [-2,-1,1,2]
    ans = 0
    tmp = 0
    for i in range(2, N-2):
        min_tmp = 255
        for j in sr:
            tmp = arr[i] - arr[i + j]
            if min_tmp > tmp:
                min_tmp = tmp
        if min_tmp > 0:
            ans += min_tmp
    print("#{} {}".format(tc,ans))