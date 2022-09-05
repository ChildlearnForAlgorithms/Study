import sys


def make_dp(n,k):
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(n+1):
        dp[i][0]=1
    for i in range(k+1):
        dp[i][i]=1

    for i in range(1,n+1):
        for j in range(1,k+1):
            dp[i][j]=dp[i-1][j]+dp[i-1][j-1]
    return dp[n][k]
T=int(sys.stdin.readline())
for i in range(T):
    k,n=map(int,sys.stdin.readline().split())
    print(make_dp(n,k))
