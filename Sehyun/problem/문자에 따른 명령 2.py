x,y=0,0
dir_num=3
dx,dy=[1,0,-1,0],[0,-1,0,1]

state=input()

for i in range(len(state)):
    if state[i]=='L':
        dir_num=(dir_num-1+4)%4
    elif state[i]=='R':
        dir_num=(dir_num+1)%4
    elif state[i]=='F':
        x, y = x + dx[dir_num], y + dy[dir_num]

print(x,y)

