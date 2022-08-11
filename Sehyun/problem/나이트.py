from collections import deque
n=int(input())
x1,y1,x2,y2=map(int,input().split())
step=[[0]*n for _ in range(n)]
visited=[[0]*n for _ in range(n)]
q=deque()
def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n
def can_go(x,y):
    if not in_range(x,y):
        return False
    if visited[x][y]:
        return False
    return True
def push(x,y,s):
    step[x][y]=s
    visited[x][y]=1
    q.append((x,y))
def bfs():
    dxs,dys=[-2,-2,-1,1,2,2,1,-1],[1,-1,-2,-2,-1,1,2,2]
    while q:
        x,y=q.popleft()
        for dx,dy in zip(dxs,dys):
            nx,ny=x+dx,y+dy
            if can_go(nx,ny):
                push(nx,ny,step[x][y]+1)
        if visited[x2-1][y2-1]:
            return
ans=-1
push(x1-1,y1-1,0)
bfs()
if visited[x2-1][y2-1]:
    ans=step[x2-1][y2-1]
print(ans)


