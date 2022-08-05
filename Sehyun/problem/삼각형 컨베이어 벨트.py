n,t=map(int,input().split())
lst=[
    list(map(int,input().split()))
    for _ in range(3)
]

for _ in range(t):
    temp=[lst[0][n-1],lst[1][n-1],lst[2][n-1]]
    for i in range(3):
        for j in range(n-1,0,-1):
            lst[i][j]=lst[i][j-1]
    lst[0][0]=temp[2]
    lst[1][0]=temp[0]
    lst[2][0]=temp[1]

for i in range(3):
    for j in range(n):
        print(lst[i][j],end=' ')
    print()
