import sys
import heapq

n = int(sys.stdin.readline())
h = []
for _ in range(n):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(h, num)
    else:
        if len(h) != 0:
            print(heapq.heappop(h)[1])
        else:
            print(0)
    print(h)
