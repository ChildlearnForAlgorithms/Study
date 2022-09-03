from math import gcd
n=int(input())
lst=list(map(int,input().split()))
for i in range(1,n):
    a=gcd(lst[0],lst[i])
    print(str(lst[0]//a)+'/'+str(lst[i]//a))