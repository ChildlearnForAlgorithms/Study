n=int(input())
a=[
    list(map(int,input().split()))
    for _ in range(n)
]
dp=[[0]*(n) for _ in range(n)]
dp[0][0]=a[0][0]
for i in range(1,n):
    dp[i][0]=a[i][0]+dp[i-1][0]
for j in range(1,n):
    dp[0][j]=a[0][j]+dp[0][j-1]
for i in range(1,n):
    for j in range(1,n):
        dp[i][j]=max(dp[i-1][j]+a[i][j],dp[i][j-1]+a[i][j])
print(dp[n-1][n-1])