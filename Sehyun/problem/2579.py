n=int(input())

stairs=[0]*(300)
for i in range(n):
    a=int(input())
    stairs[i]=a

dp=[0]*(300)

dp[0]=stairs[0]
dp[1]=stairs[0]+stairs[1]
dp[2]=max(stairs[0],stairs[1])+stairs[2]

for i in range(3,n):
    dp[i]=max(dp[i-3]+stairs[i-1]+stairs[i],dp[i-2]+stairs[i])
print(dp[n-1])