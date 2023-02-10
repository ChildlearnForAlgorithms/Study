n=int(input())
lst=[
    list(map(int,input().split()))
    for _ in range(n)
]
dp=[
    [0]*n
    for _ in range(n)
]
dp[0]=lst[0]

for i in range(1,n):
    dp[i][0]=lst[i][0]+dp[i-1][0]
    dp[0][i]=lst[0][i]+dp[0][i-1]

for i in range(1,n):
    for j in range(1,n):
        dp[i][j]=lst[i][j]+max(dp[i-1][j],dp[i][j-1])

print(dp[n-1][n-1])
