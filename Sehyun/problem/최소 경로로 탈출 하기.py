from collections import deque

n,m=map(int,input().split())

grid=[
    list(map(int,input().split()))
    for _ in range(n)
]

q=deque()
step=[
    [0]*m
    for _ in range(n)
]
visited=[
    [0]*m
    for _ in range(n)
]

def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<m

def push(x,y,s):
    step[x][y]=s
    visited[x][y]=True
    q.append((x,y))

def bfs():
    while q:
        x,y=q.popleft()
        dxs,dys=[-1,1,0,0],[0,0,-1,1]
        for dx,dy in zip(dxs,dys):
            nx,ny=x+dx,y+dy
            if in_range(nx, ny) and not visited[nx][ny] and grid[nx][ny]:
                push(nx, ny, step[x][y] + 1)

push(0,0,0)
bfs()
if visited[n-1][m-1]:
    print(step[n-1][m-1])
else:
    print(-1)
