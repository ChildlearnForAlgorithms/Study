n,m=map(int,input().split())
coin=[0]+list(map(int,input().split()))

dp=[10001]*(m+1)
dp[0]=0

for i in range(1,m+1):
    for j in range(1,n+1):
        if i>=coin[j]:
            dp[i]=min(dp[i],dp[i-coin[j]]+1)

if dp[m]==10001:
    print(-1)
else:
    print(dp[m])