n=int(input())
lst=list(map(int,input().split()))
ans=0
def prime(a):
    cnt=0
    for i in range(1,a+1):
        if a%i==0:
            cnt+=1
    return cnt

for j in range(n):
    if prime(lst[j])==2:
        ans+=1

print(ans)

