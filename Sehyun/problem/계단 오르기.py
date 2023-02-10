n=int(input())

dp=[0]*(n+1)
dp[2]=1

def stair():
    if n==2:
        print(1)
        return
    dp[3]=1
    for i in range(4,n+1):
        dp[i]=dp[i-2]+dp[i-3]
    if dp[n]:
        print(dp[n]%10007)
    else:
        print(0)

stair()