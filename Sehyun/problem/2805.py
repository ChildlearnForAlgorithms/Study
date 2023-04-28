import sys

def binary_search(height,target,start,end):
    mid = (start + end) // 2
    if start>end:
        return mid
    cnt=0
    for tree in height:
        if tree>mid:
            cnt+=(tree-mid)
    if cnt<target:
        return binary_search(height,target,start,mid-1)
    elif cnt>=target:
        return binary_search(height,target,mid+1,end)



n,m=map(int,sys.stdin.readline().split())
height=list(map(int,sys.stdin.readline().split()))



print(binary_search(height,m,0,max(height)))

