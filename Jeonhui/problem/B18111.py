import sys

N, M, B = map(int, sys.stdin.readline().split())
A = []
d = {}
for i in range(N):
    A += list(map(int, sys.stdin.readline().split()))

for i in range(len(A)):
    if A[i] not in d:
        d[A[i]] = 1
    else:
        d[A[i]] += 1

h = sorted(d.keys())

for i in range(h[0], h[-1] + 1):
    res = 0
    b = B
    for x in h:
        if x > i:
            res += (x-i) * d[x]
            b -= x
        else:

