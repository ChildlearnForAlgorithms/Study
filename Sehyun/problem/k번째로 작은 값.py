import sys,heapq

A=list(map(int,sys.stdin.readline().split()))
n=len(A)
heap=[]
m=[-sys.maxsize-1]*n
m[0]=A[0]

for i in range(1,n):
    for j in range(0,i+1):
        heapq.heappush(heap,A[j])
    k=i//3+1
    for l in range(k-1):
        heapq.heappop(heap)
    a=heapq.heappop(heap)
    m[i]=a
    heap=[]

print(sum(m))

