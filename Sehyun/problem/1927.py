import heapq
import sys

n=int(input())
lst=[]

for i in range(n):
    a=int(sys.stdin.readline())
    if a==0:
        if len(lst)==0:
            print(0)
        else:
            print(heapq.heappop(lst))
    else:
        heapq.heappush(lst,a)