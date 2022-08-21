import sys

n = int(sys.stdin.readline())
direction = list(map(int, sys.stdin.readline().split()))
oil = list(map(int, sys.stdin.readline().split()))
res = 0
min_oil = oil[0]
for i in range(1, n):
    res += (direction[i - 1] * min_oil)
    if min_oil > oil[i]:
        min_oil = oil[i]
print(res)
