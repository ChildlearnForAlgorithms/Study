import sys


def find(x):
    if len(d[x]) == 0 or x in virus:
        return
    else:
        virus[x] = 1
        for i in range(len(d[x])):
            find(d[x][i])


d = {}
virus = {}
c = int(sys.stdin.readline())
n = int(sys.stdin.readline())
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    if a not in d:
        d[a] = [b]
    else:
        d[a].append(b)
    if b not in d:
        d[b] = [a]
    else:
        d[b].append(a)
find(1)
print(len(virus.keys()) - 1)
