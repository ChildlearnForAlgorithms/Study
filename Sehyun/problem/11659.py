import sys

n,m=map(int,sys.stdin.readline().split())

lst=list(map(int,sys.stdin.readline().split()))

sum_lst=[0]*n
sum_lst[0]=lst[0]

for i in range(1,n):
    sum_lst[i]=sum_lst[i-1]+lst[i]

for _ in range(m):
    i,j=map(int,sys.stdin.readline().split())
    if i==1:
        print(sum_lst[j-1])
    elif i==j:
        print(lst[j-1])
    else:
        print(sum_lst[j-1]-sum_lst[i-2])

#1 3 6