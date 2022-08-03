n=int(input())
x,y=0,0
dx,dy=[1,0,-1,0],[0,-1,0,1]
mapper={
    'E':0,
    'S':1,
    'W':2,
    'N':3
}
cnt=0
ans=-1
def move(dir_num,distance):
    global x,y
    global ans,cnt
    for _ in range(distance):
        x,y=x+dx[dir_num],y+dy[dir_num]
        cnt+=1
        if x==0 and y==0:
            ans=cnt
            return True
    return False

for _ in range(n):
    direction, distance = input().split()
    distance = int(distance)
    dir_num = mapper[direction]
    done=move(dir_num,distance)
    if done:
        break
print(ans)



