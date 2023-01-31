x,y=0,0
dx,dy=[1,0,-1,0],[0,-1,0,1]
dir_num=0
state=input()

flag=False

for i in range(len(state)):
    if state[i]=='L':
        dir_num=(dir_num-1+4)%4
    elif state[i]=='R':
        dir_num=(dir_num+1)%4
    elif state[i]=='F':
        x,y=x+dx[dir_num],y+dy[dir_num]
    if x==0 and y==0:
        flag=True
        print(i+1)
        break

if flag==False:
    print(-1)
