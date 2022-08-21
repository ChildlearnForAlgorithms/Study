import sys

n, m = map(int, sys.stdin.readline().split())

poketmon = {}
for i in range(1,n+1):
    a=sys.stdin.readline().strip()
    poketmon[i]=a
    poketmon[a]=i

for i in range(m):
    b = sys.stdin.readline().strip()
    if b.isdigit():
        b=int(b)
        print(poketmon[b])
    else:
        print(poketmon[b])
