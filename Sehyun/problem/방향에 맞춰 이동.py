n=int(input())
x,y=0,0
dx,dy=[-1,0,0,1],[0,-1,1,0]
dir_num_lst=[]
for _ in range(n):
    a,b=input().split()
    b=int(b)
    dir_num=0
    if a=='W':
        dir_num=0
    elif a=='S':
        dir_num=1
    elif a == 'N':
        dir_num=2
    elif a=='E':
        dir_num=3
    x, y = x + b * dx[dir_num], y + b * dy[dir_num]
print(x,y)