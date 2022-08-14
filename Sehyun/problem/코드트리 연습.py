from collections import deque
n,m=map(int,input().split())
grid=[list(map(int,input().split())) for _ in range(n)]
q=deque()
step=[[0]*m for _ in range(n)]
visited=[[False]*m for _ in range(n)]
def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n
def push(x,y,s):
    step[x][y]=s
    visited[x][y]=True
    q.append((x,y))
def bfs():
    dxs,dys=[-1,1,0,0],[0,0,-1,1]
    while q:
        x,y=q.popleft()
        for dx,dy in zip(dxs,dys):
            nx,ny=x+dx,y+dy
            if in_range(nx,ny) and not visited[nx][ny]\
                and grid[nx][ny]>0:
                push(nx,ny,step[nx][ny]+1)
for i in range(n):
    for j in range(m):
        if grid[i][j]>0:
            push(i,j,0)
            bfs()
            print(step[nx][ny])