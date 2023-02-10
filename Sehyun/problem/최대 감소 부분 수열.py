n=int(input())
lst=list(map(int,input().split()))
reversed_lst=[0]+lst[::-1]

dp=[0]*(n+1)


for i in range(1,n+1):
    for j in range(i):
        if reversed_lst[j]<reversed_lst[i]:
            dp[i]=max(dp[i],dp[j]+1)

print(max(dp))