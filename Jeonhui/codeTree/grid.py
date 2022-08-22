import sys

MOVE = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def getCheckPos(x, y, n):
    return [(x + moveX, y + moveY) for moveX, moveY in MOVE if 0 <= x + moveX < n and 0 <= y + moveY < n]

n, m = map(int, sys.stdin.readline().split())
pos = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]
check = {}

for x, y in pos:
    check[(x - 1, y - 1)] = True
    res = [check.get(around) for around in getCheckPos(x-1,y-1,n) if check.get(around) is not None]
    print(1 if len(res) == 3 else 0)