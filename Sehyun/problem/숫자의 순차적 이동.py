n,m=map(int,input().split())
grid=[list(map(int,input().split())) for _ in range(n)]

dxs,dys=[-1, -1, -1,  0, 0,  1, 1, 1],[-1,  0,  1, -1, 1, -1, 0, 1]

def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n

def find_pos(num):
    for i in range(n):
        for j in range(n):
            if grid[i][j]==num:
                return (i,j)

def next_pos(pos):
    max_num = 0
    max_pos=0,0
    x,y=pos
    for dx,dy in zip(dxs,dys):
        nx,ny=x+dx,y+dy
        if in_range(nx,ny) and grid[nx][ny]>max_num:
            max_num=grid[nx][ny]
            max_pos=(nx,ny)
    return max_pos

def swap(pos,max_pos):
    (x,y),(nx,ny)=pos,max_pos
    grid[x][y],grid[nx][ny]=grid[nx][ny],grid[x][y]

def find_num():
    for i in range(1,n*n+1):
        pos=find_pos(i)
        max_pos=next_pos(pos)
        swap(pos,max_pos)

for _ in range(m):
    find_num()

for i in range(n):
    for j in range(n):
        print(grid[i][j],end=" ")
    print()