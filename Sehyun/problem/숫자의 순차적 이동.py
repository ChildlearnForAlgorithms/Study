n,m=map(int,input().split())
grid=[list(map(int,input().split())) for _ in range(n)]

dxs,dys=[-1,1,0,0,-1,1,1,-1],[0,0,-1,1,-1,-1,1,1]

def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n

def great_num(n,num):
    max_num=-1
    max_pos_x,max_pos_y=-1,-1
    for i in range(n):
        for j in range(n):
            if grid[i][j]==num:
                for dx,dy in zip(dxs,dys):
                    nx,ny=i+dx,j+dy
                    if in_range(nx,ny) and grid[nx][ny]>max_num:
                        max_num=grid[nx][ny]
                        max_pos_x,max_pos_y=nx,ny
                grid[i][j],grid[max_pos_x][max_pos_y]=\
                    grid[max_pos_x][max_pos_y],grid[i][j]
                return


def exchange():
    for num in range(1,n*n+1):
        great_num(n,num)

for _ in range(m):
    exchange()

for i in range(n):
    for j in range(n):
        print(grid[i][j],end=' ')
    print()