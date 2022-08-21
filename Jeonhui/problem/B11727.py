import sys

n = int(sys.stdin.readline())
DP = []
j = 1
res = 0
while j ** 2 <= n:
    DP.append(j ** 2)
    j += 1

while n > 0:
    print(n, end=" ")
    for i in range(len(DP)):
        if DP[i] > n:
            res += 1
            n -= DP[i - 1]
            print(DP[i - 1], DP[i], res)
            break
        if DP[i] == n or i == len(DP) - 1:
            res += 1
            n -= DP[i]
            print(DP[i],res)
            break
print(res)
