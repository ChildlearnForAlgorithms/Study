n=int(input())

dx,dy=[-1,0,0,1],[0,-1,1,0]

mapper={
    'W':0,
    'S':1,
    'N':2,
    'E':3
}

x,y=0,0

flag=False

cnt=0

for i in range(n):
    a,b=input().split()
    b=int(b)
    for j in range(b):
        x,y=x+dx[mapper[a]],y+dy[mapper[a]]
        if x==0 and y==0:
            flag=True
            cnt+=1
            print(cnt)
            break
        else:
            cnt+=1
    if flag==True:
        break

if flag==False:
    print(-1)
