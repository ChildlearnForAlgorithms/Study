import sys,heapq

def find(A,k):
    for i in range(k-1):
        A[0]=A[-1]
        A.pop()
        m=0
        while 2*m+1<len(A):
            left,right=2*m+1,2*m+2
            smaller=left
            if right<len(A):
                if A[right]<A[left]:
                    smaller=right
            if A[m]>A[smaller]:
                A[m],A[smaller]=A[smaller],A[m]
                m=smaller
            else:
                break
    return A[0]

A=list(map(int,sys.stdin.readline().split()))
n=len(A)

m=[-sys.maxsize-1]*n

for i in range(n):
    sliced_A=A[:i+1]
    heapq.heapify(sliced_A)
    k=i//3+1
    m[i]=find(sliced_A,k)

print(sum(m))