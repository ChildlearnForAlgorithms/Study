N=int(input())
a=list(map(int,input().split()))
a.sort()
if len(a)%2==0:
    n=len(a)//2
    print(a[n-1]*a[n])
elif len(a)==1:
    print(a[0]**2)
else:
    n=len(a)//2
    print(a[n]**2)