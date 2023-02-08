from collections import deque

n,m=map(int,input().split())
grid=[
    list(map(int,input().split()))
    for _ in range(n)
]
visited=[[0]*m for _ in range(n)]
q=deque()

def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<m

def can_go(x,y):
    if not in_range(x,y):
        return False
    if visited[x][y] or grid[x][y]==0:
        return False
    return True

def bfs():
    while q:
        x,y=q.popleft()
        dxs,dys=[0,1,0,-1],[1,0,-1,0]
        for dx,dy in zip(dxs,dys):
            nx,ny=x+dx,y+dy
            if can_go(nx,ny):
                q.append((nx,ny))
                visited[nx][ny]=True

visited[0][0]=True
q.append((0,0))
bfs()

if visited[n-1][m-1]:
    print(1)
else:
    print(0)