import math

T=int(input())
for i in range(T):
    cnt=0
    x1,y1,x2,y2=map(int,input().split())
    n=int(input())
    for j in range(n):
        cx,cy,r=map(int,input().split())
        distance1=math.sqrt((cx-x1)**2+(cy-y1)**2)
        distance2=math.sqrt((cx-x2)**2+(cy-y2)**2)
        if (distance1<r and distance2>r) or (distance1>r and distance2<r):
            cnt+=1
    print(cnt)