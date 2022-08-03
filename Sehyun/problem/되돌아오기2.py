lst=list(input())
dx,dy=[0,1,0,-1],[1,0,-1,0]
x,y=0,0
dir_num=0
flag=False
for i in range(len(lst)):
    if lst[i]=='F':
        x,y=x+dx[dir_num],y+dy[dir_num]
    elif lst[i]=='R':
        dir_num=(dir_num+1)%4
    elif lst[i]=='L':
        dir_num=(dir_num-1+4)%4
    if x==0 and y==0:
        print(i+1)
        flag=True
        break
if flag==False:
    print(-1)



