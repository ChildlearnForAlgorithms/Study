n=int(input())
lst=[0]
for i in range(n):
    a=int(input())
    lst.append(a)

dp=[0]

dp.append(lst[1])
if n>1:
    dp.append(lst[1]+lst[2])
for i in range(3,n+1):
    dp.append(max(dp[i-1],dp[i-3]+lst[i-1]+lst[i],dp[i-2]+lst[i]))

print(dp[n])
