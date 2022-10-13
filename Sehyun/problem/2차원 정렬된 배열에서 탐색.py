import sys

n,k=map(int,sys.stdin.readline().split())

lst=[
    list(map(int,sys.stdin.readline().split()))
    for _ in range(n)
]

bool=False

def binary_search(A,k):
    global bool
    l,r=0,n
    while r-l>=0:
        m=(l+r)//2
        if A[m]>k:
            r=m-1
        elif A[m]<k:
            l=m+1
        elif A[m]==k:
            bool=True
            return m


m=0
for i in range(n):
    A=lst[i]
    for j in range(n):
        m=binary_search(A,k)
    if bool==False:
        continue
    elif bool==True:
        print((i,m))
        break

