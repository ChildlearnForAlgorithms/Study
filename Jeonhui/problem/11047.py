import sys

N, K = map(int, sys.stdin.readline().split())
coins = reversed([int(sys.stdin.readline()) for _ in range(N)])
res = 0
for coin in coins:
    res += K//coin
    K%=coin
print(res)