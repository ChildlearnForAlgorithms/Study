import sys

n = int(sys.stdin.readline())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
DP = [[0, 0, 0] for _ in range(n)]
DP[0] = A[0]
for i in range(1, n):
    DP[i][0] = min(DP[i - 1][1], DP[i - 1][2]) + A[i][0]
    DP[i][1] = min(DP[i - 1][0], DP[i - 1][2]) + A[i][1]
    DP[i][2] = min(DP[i - 1][0], DP[i - 1][1]) + A[i][2]
print(min(DP[n - 1]))
