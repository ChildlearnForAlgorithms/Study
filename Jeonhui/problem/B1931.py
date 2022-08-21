import sys

n = int(sys.stdin.readline())
A = []
for i in range(n):
    A.append(list(map(int, sys.stdin.readline().split())))
A = sorted(A, key=lambda x: (x[1],x[0]))
L = [0]
for i in range(1, n):
    if A[L[-1]][1] <= A[i][0]:
        L.append(i)
print(len(L))
