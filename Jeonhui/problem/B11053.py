import sys

n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

DP = [1] * n
for i in range(1, n):
    for j in range(i, -1, -1):
        if DP[j] >= DP[i] and A[i] > A[j]:
            DP[i] = DP[j] + 1
print(max(DP))

'''
10 20 10 30 20 50
 1  2 1
'''
