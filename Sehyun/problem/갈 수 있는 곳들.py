from collections import deque
n,k=map(int,input().split())
grid=[list(map(int,input().split())) for _ in range(n)]
visited=[[0]*n for _ in range(n)]
q=deque()
def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n
def can_go(x,y):
    if not in_range(x,y):
        return False
    if visited[x][y] or grid[x][y]==1:
        return False
    return True

def bfs():
    dxs,dys=[-1,1,0,0],[0,0,-1,1]
    while q:
        x,y=q.popleft()
        for dx,dy in zip(dxs,dys):
            nx,ny=x+dx,y+dy
            if can_go(nx,ny):
                visited[nx][ny]=True
                q.append((nx,ny))

for _ in range(k):
    x,y=map(int,input().split())
    q.append((x-1,y-1))
    visited[x-1][y-1]=True
bfs()
print(sum([1
          for i in range(n)
          for j in range(n)
          if visited[i][j]]))

