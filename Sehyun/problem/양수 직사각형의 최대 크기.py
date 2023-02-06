n,m=map(int,input().split())

grid=[
    list(map(int,input().split()))
    for _ in range(n)
]
ysize_lst=[]
xsize_lst=[]
size_lst=[]

for i in range(n):
    for j in range(m):
        a,b=i,j
        while b<m and grid[a][b]>0:
            b+=1
            if b>=m or grid[a][b]<=0:
                ysize_lst.append(b-j)
                break
        while a<n and grid[a][ysize_lst[-1]-1]>0:
            a+=1
            if a>=n or grid[a][ysize_lst[-1]-1]<=0:
                xsize_lst.append(a-i)
                break
        size_lst.append(xsize_lst[-1]*ysize_lst[-1])
        # print(ysize_lst[-1],xsize_lst[-1],size_lst[-1])
print(max(size_lst))