n=int(input())

lst=[]

for _ in range(n):
    a=list(map(int,input().split()))
    lst.append(a)

dp=[[0]*n for _ in range(n)]
dp[0][0]=lst[0][0]

for i in range(1,n):
    dp[i][0]=lst[i][0]+dp[i-1][0]

for i in range(1,n):
    dp[i][i]=lst[i][-1]+dp[i-1][i-1]

for i in range(2,n):
    for j in range(i-1,0,-1):
        dp[i][j]=max(dp[i-1][j-1],dp[i-1][j])+lst[i][j]

answer=[]

for i in range(n):
    answer.append(dp[n-1][i])

print(max(answer))



