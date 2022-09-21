lst=[input() for _ in range(2)]

dp=[[0]*(len(lst[1])+1) for _ in range(len(lst[0])+1)]

for i in range(1,len(lst[0])+1):
    for j in range(1,len(lst[1])+1):
        if lst[0][i-1]==lst[1][j-1]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i][j-1],dp[i-1][j])

print(dp[-1][-1])
