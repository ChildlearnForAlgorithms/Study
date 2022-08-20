import sys
n=int(sys.stdin.readline())
lst=list(map(int,sys.stdin.readline().split()))
arr=sorted(list(set(lst)))
dic={arr[i]:i for i in range(len(arr))}
for i in lst:
    print(dic[i],end=' ')