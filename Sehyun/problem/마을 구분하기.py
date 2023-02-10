n=int(input())
grid=[
    list(map(int,input().split()))
    for _ in range(n)
]
visited=[[0]*n for _ in range(n)]
dxs,dys=[-1,1,0,0],[0,0,-1,1]

def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n

def can_go(x,y):
    if not in_range(x,y):
        return False
    if visited[x][y] or grid[x][y]==0:
        return False
    return True

def dfs(x,y):
    global num
    for dx,dy in zip(dxs,dys):
        nx,ny=x+dx,y+dy
        if can_go(nx,ny):
            visited[nx][ny]=1
            num+=1
            dfs(nx,ny)

cnt=0
lst=[]

def simulate(x,y):
    global cnt,num
    num=1
    dfs(x,y)
    lst.append(num)
    cnt+=1

for i in range(n):
    for j in range(n):
        if visited[i][j]==0 and grid[i][j]==1:
            visited[i][j]=1
            simulate(i,j)

lst.sort()
print(cnt)
for elem in lst:
    print(elem)