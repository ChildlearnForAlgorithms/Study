import sys

n = int(sys.stdin.readline())
A = [int(sys.stdin.readline()) for _ in range(n)]
DP = [[0] * n for _ in range(n)]

''' 1칸 1,1칸 2칸
10      35  50
    30      60
    20  35  55
'''

DP[0][0] = A[0]
DP[1][1] = A[0] + A[1]
DP[1][2] = A[1]
DP[2][0] = A[1] + A[2]
DP[2][2] = A[0] + A[2]

for i in range(3, n):
    DP[i][0] = DP[i - 1][2] + A[i]
    DP[i][1] = DP[i - 1][0] + A[i]
    DP[i][2] = max(DP[i - 2]) + A[i]

print(A)
for i in range(n):
    print(DP[i][0],end=" ")
print()
for i in range(n):
    print(DP[i][1],end=" ")
print()
for i in range(n):
    print(DP[i][2],end=" ")