import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque([])
for _ in range(n):
    a = sys.stdin.readline().split()
    if a[0] == "push":
        queue.append(a[1])
    elif a[0] == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
            queue.popleft()
    elif a[0] == "size":
        print(len(queue))
    elif a[0] == "empty":
        print(1 if len(queue) == 0 else 0)
    elif a[0] == "front":
        print(queue[0] if len(queue) != 0 else -1)
    elif a[0] == "back":
        print(queue[len(queue) - 1] if len(queue) != 0 else -1)
