def solve(L, S):
    dp = [[0] * (1001) for _ in range(1001)]
    for j in range(1,10):
        dp[1][j]=1
    for i in range(1,10):
        dp[i][1]=1
    for i in range(2, 1001):
        for j in range(2, 10):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    for i in range(2,1001):
        for j in range(10,1001):
            sum=0
            for k in range(j-9,j+1):
                sum+=dp[i-1][k]
            dp[i][j]=sum
    return dp[L][S]


L, S = [int(x) for x in input().split()]

print(solve(L, S) % 2147483647)