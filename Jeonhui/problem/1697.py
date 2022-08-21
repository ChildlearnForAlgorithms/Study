import sys
from collections import deque

visited = [-1] * 100001


def bfs(N, K):
    queue = deque([x])
    visited[x] = 0

    while queue:
        v = queue.popleft()
        if v == y:
            print(visited[v])
            break

        if 0 <= (v - 1) <= 100000 and visited[v - 1] == -1:
            queue.append(v - 1)
            visited[v - 1] = visited[v] + 1
        if 0 <= (v + 1) <= 100000 and visited[v + 1] == -1:
            queue.append(v + 1)
            visited[v + 1] = visited[v] + 1
        if 0 <= (v * 2) <= 100000 and visited[v * 2] == -1:
            queue.append(v * 2)
            visited[v * 2] = visited[v] + 1


x, y = map(int, sys.stdin.readline().split())
bfs(x, y)
