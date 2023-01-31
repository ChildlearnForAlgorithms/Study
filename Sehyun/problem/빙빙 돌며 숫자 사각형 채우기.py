n,m=map(int,input().split())
grid=[[0]*m for _ in range(n)]
grid[0][0]=1
x,y=0,0
dir_num=0
dx,dy=[0,1,0,-1],[1,0,-1,0]


def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<m

for i in range(2,n*m+1):
    nx,ny=x+dx[dir_num],y+dy[dir_num]
    if in_range(nx,ny) and not grid[nx][ny]:
        x,y=nx,ny
        grid[x][y]=i
    else:
        dir_num=(dir_num+1)%4
        nx, ny = x + dx[dir_num], y + dy[dir_num]
        x,y=nx,ny
        grid[x][y] = i

for i in range(n):
    for j in range(m):
        print(grid[i][j],end=" ")
    print()

