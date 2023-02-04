n,m,t=map(int,input().split())

grid=[
    list(map(int,input().split()))
    for _ in range(n)
]

dxs,dys=[-1,1,0,0],[0,0,-1,1]
count=[[0]*n for _ in range(n)]
lst=[[0]*n for _ in range(n)]


def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n

def change(x,y):
    max_val = 0
    max_x, max_y = 0,0
    for dx,dy in zip(dxs,dys):
        nx,ny=x+dx,y+dy
        if in_range(nx,ny) and grid[nx][ny]>max_val:
            max_x,max_y=nx,ny
            max_val=grid[nx][ny]
    lst[max_x][max_y]+=1


def move_all():
    for i in range(n):
        for j in range(n):
            lst[i][j]=0
    for i in range(n):
        for j in range(n):
            if count[i][j]==1:
                change(i,j)
    for i in range(n):
        for j in range(n):
            count[i][j] = lst[i][j]

def check():
    for i in range(n):
        for j in range(n):
            if count[i][j]>=2:
                count[i][j]=0
def simulate():
    move_all()
    check()

for _ in range(m):
    x,y=map(int,input().split())
    x,y=x-1,y-1
    count[x][y]=1

for _ in range(t):
    simulate()

cnt=0
for i in range(n):
    for j in range(n):
        cnt+=count[i][j]
print(cnt)