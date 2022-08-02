n,t=map(int,input().split())
r,c,d=input().split()
r,c=int(r)-1,int(c)-1

dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]
dir_num=0
if d=='L':
    dir_num=3
elif d=='R':
    dir_num=0
elif d=='U':
    dir_num=2
elif d=='D':
    dir_num=1

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

for _ in range(t):
    nx,ny=r+dxs[dir_num],c+dys[dir_num]
    if in_range(nx,ny):
        r,c=nx,ny
    else:
        dir_num=3-dir_num
print(r+1,c+1)