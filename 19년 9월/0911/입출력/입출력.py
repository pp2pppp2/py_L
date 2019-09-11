import sys
sys.stdin = open("input.txt")

T = input()
R, C = input().split()
print(T)
print("{} {}".format(R,C))
for i in range(5):
    data = input()
    print(data)