import sys

n=int(sys.stdin.readline())

lst=list(map(int,sys.stdin.readline().split()))

ans=sys.maxsize

def find_min(idx,cnt,sub):
    global ans

    if idx==2*n:
        if cnt==n:
            ans=min(ans,abs(sub))
        return

    find_min(idx+1,cnt+1,sub+lst[idx])
    find_min(idx+1,cnt,sub-lst[idx])

find_min(0,0,0)
print(ans)