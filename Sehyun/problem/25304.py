X=int(input())
n=int(input())
lst=[]
for i in range(n):
    x,y=map(int,input().split())
    lst.append(x*y)

if sum(lst)==X:
    print('Yes')
else:
    print('No')
