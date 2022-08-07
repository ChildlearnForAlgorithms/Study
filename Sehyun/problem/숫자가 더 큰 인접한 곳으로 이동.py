n,x,y=map(int,input().split())
x,y=x-1,y-1
grid=[
    list(map(int,input().split()))
    for _ in range(n)
]
dxs,dys=[-1,1,0,0],[0,0,-1,1]

def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n

def can_move(x,y,temp):
    return in_range(x,y) and grid[x][y]>temp
temp_lst = [grid[x][y]]
def move():
    global x,y
    global dx,dy
    for dx,dy in zip(dxs,dys):
        nx,ny=x+dx,y+dy
        if can_move(nx,ny,grid[x][y]):
            x,y=nx,ny
            return True
    return False

while True:
    simulate=move()
    if not simulate:
        break
    temp_lst.append(grid[x][y])
for num in temp_lst:
    print(num,end=' ')