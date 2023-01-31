n=int(input())

grid=[
    list(map(int,input().split()))
    for _ in range(n)
]

def in_range(x,y):
    return x>=0 and x<n and y>=0 and y<n

dxs,dys=[1,-1,0,0],[0,0,1,-1]
total=0
for i in range(n):
    for j in range(n):
        cnt=0
        for dx,dy in zip(dxs,dys):
            nx,ny=i+dx,j+dy
            if in_range(nx,ny) and grid[nx][ny]==1:
                cnt+=1
        if cnt>=3:
            total+=1

print(total)



