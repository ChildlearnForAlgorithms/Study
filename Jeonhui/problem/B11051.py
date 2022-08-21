"""
import sys

n, k = map(int, sys.stdin.readline().split())
dp = [1] + [0] * (n - k)
for i in range(1, n - k + 1):
    dp[i] = dp[i - 1] * (n - i + 1) // i
print(dp[n - k] % 10007)
"""
# B1934
"""
import sys

n = int(sys.stdin.readline())
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    x = a * b
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    print(x//a)
"""

"""
import sys

n = int(sys.stdin.readline())
print(" ".join(list(map(str, sorted(list(set(list(map(int, sys.stdin.readline().split())))))))))

"""

import sys

n = int(sys.stdin.readline())
A = sorted(list(map(int, sys.stdin.readline().split())))
res = 0
dp = [A[0]] + [0] * (n - 1)
for i in range(1, n):
    dp[i] = dp[i - 1] + A[i]
print(sum(dp))
