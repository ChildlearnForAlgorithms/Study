def solve(L, S):
    dp=[[0]*10001 for _ in range(1001)]
    for i in range(1,1001):
        for j in range(1,1001):
            if j==1 or j==i:
                dp[i][j]=1
            else:
                dp[i][j]=dp[i-1][j-1]+dp[i-j][j]
    return dp[S][L]




L, S = [int(x) for x in input().split()]
print(solve(L, S)%2147483647)
#math.perm(n, r)