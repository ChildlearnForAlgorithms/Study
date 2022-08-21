import sys

n = int(sys.stdin.readline())
A = []
for i in range(n):
    A.append(list(map(int, sys.stdin.readline().split())))
DP = list([0] * i for i in range(1, n + 1))
DP[0][0] = A[0][0]
for i in range(1, n):
    DP[i][0] = DP[i - 1][0] + A[i][0]
    for j in range(1, i):
        DP[i][j] = max(DP[i - 1][j - 1], DP[i - 1][j]) + A[i][j]
    DP[i][i] = DP[i - 1][i - 1] + A[i][i]
print(max(DP[n-1]))
