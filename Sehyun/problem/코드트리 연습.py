n=int(input())
grid=[]
for i in range(n):
    a=list(map(int,input().split()))
    grid.append(a)

cnt_lst=[]

for i in range(n):
    for j in range(n):
        cnt=0
        for k in range(i,i+3):
            for m in range(j,j+3):
                if i+3<=n and j+3<=n and grid[k][m]==1:
                    print(i,j,k,m)
                    cnt+=1
        cnt_lst.append(cnt)

print(max(cnt_lst))