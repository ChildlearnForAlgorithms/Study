n,m=map(int,input().split())
lst=list(map(int,input().split()))
ans=0

def select(curr_idx,curr_num,curr_val):
    global ans
    if curr_num==m:
        ans=max(ans,curr_val)
        return
    if curr_idx==n:
        return
    select(curr_idx+1,curr_num+1,curr_val^lst[curr_idx])

    select(curr_idx+1,curr_num,curr_val)

select(0,0,0)

print(ans)


