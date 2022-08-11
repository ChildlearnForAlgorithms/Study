import sys
sys.setrecursionlimit(2500)
n,m=map(int,input().split())
grid=[
    list(map(int,input().split()))
    for _ in range(n)
]
visited=[[False]*m for _ in range(n)]
cnt=0
def init_visited():
    for i in range(n):
        for j in range(m):
            visited[i][j]=False
def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<m

def can_go(x,y,k):
    if not in_range(x,y):
        return False
    if visited[x][y] or grid[x][y]<=k:
        return False
    return True

def dfs(x,y,k):
    dxs,dys=[-1,1,0,0],[0,0,-1,1]
    for dx,dy in zip(dxs,dys):
        nx,ny=x+dx,y+dy
        if can_go(nx,ny,k):
            visited[nx][ny]=True
            dfs(nx,ny,k)

def simulation(k):
    global cnt
    cnt=0
    init_visited()
    for i in range(n):
        for j in range(m):
            if can_go(i,j,k):
                visited[i][j]=True
                cnt+=1
                dfs(i,j,k)
    return cnt
max_num=-1
answer_k=0
for k in range(1,101):
    simulation(k)
    if cnt>max_num:
        max_num,answer_k=cnt,k

print(answer_k,max_num)