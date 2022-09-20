n=int(input())
lst=[
    list(map(int,input().split()))
    for _ in range(n)
]

lst.sort(key=lambda x:x[0])

b_lst=[]
for i in range(n):
    b_lst.append(lst[i][1])

dp=[1]*(n)
dp[0]=1

for i in range(0,n):
    for j in range(i):
        if b_lst[j]<b_lst[i]:
            dp[i]=max(dp[i],dp[j]+1)

print(n-max(dp))