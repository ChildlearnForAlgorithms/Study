n=int(input())
a=list(map(int,input().split()))
dp1=[1]*n
dp2=[1]*n
reversed_a=a[::-1]

for i in range(1,n):
    for j in range(i):
        if a[j]<a[i]:
            dp1[i]=max(dp1[i],dp1[j]+1)

for i in range(1,n):
    for j in range(i):
        if reversed_a[j]<reversed_a[i]:
            dp2[i]=max(dp2[i],dp2[j]+1)

answer=[0]*n
for i in range(n):
    answer[i]=dp1[i]+dp2[n-1-i]-1

print(max(answer))