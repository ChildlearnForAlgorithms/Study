import sys

n = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))

# prefixsum
DP = [A[0]] + ([0] * (n - 1))
for i in range(1, n):
    DP[i] = DP[i - 1] + A[i] if DP[i - 1] + A[i] > A[i] else A[i]
print(max(DP))