import sys

def binary_search(array,height,target,start,end):
    while start<=end:
        mid=(start+end)//2
        print(sum([x-array[mid] for x in height if x>array[mid]]),array[mid],target)
        if target==sum([x-array[mid] for x in height if x>array[mid]]):
            return array[mid]
        elif sum([x-array[mid] for x in height if x>array[mid]])>target:
            start=mid+1
        else:
            end=mid-1
    return None

n,m=map(int,sys.stdin.readline().split())
height=list(map(int,sys.stdin.readline().split()))
lst=[x for x in range(1,max(height))]
lst.sort()
print(lst)


print(binary_search(lst,height,m,0,len(lst)-1))

