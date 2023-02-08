n,m,k=map(int,input().split())
dist=list(map(int,input().split()))
result=[1]*k
ans=0
def calc():
    ans=0
    for i in range(k):
        ans+=(result[i]>=m)
    return ans

def select(cnt):
    global ans

    ans=max(ans,calc())

    if cnt==n:
        return

    for i in range(k):
        if result[i]>=m:
            continue

        result[i]+=dist[cnt]
        select(cnt+1)
        result[i]-=dist[cnt]

select(0)
print(ans)