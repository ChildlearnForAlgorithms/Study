n,m=map(int,input().split())
grid=[[0 for _ in range(n+1)] for _ in range(n+1)]
dxs,dys=[1,-1,0,0],[0,0,1,-1]

def in_range(x,y):
    return 1<=x and x<n+1 and 1<=y and y<n+1


for _ in range(m):
    cnt=0
    x,y=map(int,input().split())
    grid[x][y]=1
    for i in range(4):
        nx,ny=0,0
        nx,ny=x+dxs[i],y+dys[i]
        if in_range(nx,ny):
            if grid[nx][ny]==1:
                cnt+=1
    if cnt==3:
        print(1)
    else:
        print(0)


