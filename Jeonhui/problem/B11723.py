import sys

s = set([])
n = int(sys.stdin.readline())
for _ in range(n):
    c = list(map(str, sys.stdin.readline().split()))
    if c[0] == "add":
        s.add(int(c[1]))
    elif c[0] == "remove":
        if int(c[1]) in s:
            s.remove(int(c[1]))
    elif c[0] == "check":
        print(1 if int(c[1]) in s else 0)
    elif c[0] == "toggle":
        if int(c[1]) in s:
            s.remove(int(c[1]))
        else:
            s.add(int(c[1]))
    elif c[0] == "all":
        s = set(list(range(1, 21)))
    elif c[0] == "empty":
        s = set([])
