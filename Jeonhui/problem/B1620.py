import sys

n, m = map(int, sys.stdin.readline().split())
pkm = {}
for i in range(n):
    p = sys.stdin.readline().rstrip()
    pkm[p] = str(i + 1)
    pkm[str(i + 1)] = p
for i in range(m):
    q = sys.stdin.readline().rstrip()
    print(pkm[q])
