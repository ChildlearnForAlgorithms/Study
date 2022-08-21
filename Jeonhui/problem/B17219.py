import sys

d = {}
n, m = map(int, sys.stdin.readline().split())
for _ in range(n):
    site, password = map(str, sys.stdin.readline().split())
    d[site] = password
for _ in range(m):
    print(d[sys.stdin.readline().rstrip()])
