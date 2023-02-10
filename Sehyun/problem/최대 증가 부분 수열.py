n=int(input())
lst=[0]+list(map(int,input().split()))
dp=[0]*(n+1)

for i in range(1,n+1):
    for j in range(i):
        if lst[i]>lst[j]:
            dp[i]=max(dp[j]+1,dp[i])

print(max(dp))