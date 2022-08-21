import sys
from collections import deque

queue = deque()
print(queue)


def find_way(x, y):
    visit = A[:]
    while True:
        if x == m - 1 and y == n - 1:
            return len(queue)
        if x < n and A[x + 1][y] == 1:
            x += 1
            queue.append((x, y))


n, m = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
q = [[0] * m for _ in range(n)]
find_way(0, 0)
