import heapq
from sys import stdin

A = list(map(int,stdin.readline().split()))

ans = 0
small = []  # max-heap
big = []  # min-heap

for idx, val in enumerate(A, start=1):
    if big and (idx != 1 and idx % 3 == 1):
        val2=heapq.heappop(big)
        heapq.heappush(small, (-val2,val2))

    heapq.heappush(small, (-val,val))
    heapq.heappush(big, heapq.heappop(small)[1])
    ans += big[0]

print(ans)


#9 1 3 2 7 0 -2 4 5