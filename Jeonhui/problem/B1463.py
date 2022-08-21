import sys

n = int(sys.stdin.readline())
A = [0, 0, 1, 1]
for i in range(4, n + 1):
    x = (i // 2 if i % 2 == 0 else i - 1)
    y = (i // 3 if i % 3 == 0 else i - 1)
    A.append(min(A[i - 1] + 1, A[x] + 1, A[y] + 1))
print(A[n])
