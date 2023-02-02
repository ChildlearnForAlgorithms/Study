n,t=map(int,input().split())
grid=[
    list(map(int,input().split()))
    for _ in range(2)
]
def change():
    temp1=grid[0][-1]
    temp2=grid[1][-1]

    for i in range(n-1,0,-1):
        grid[0][i]=grid[0][i-1]

    grid[0][0]=temp2

    for i in range(n-1,0,-1):
        grid[1][i]=grid[1][i-1]

    grid[1][0]=temp1

for i in range(t):
    change()

for i in range(2):
    for j in range(n):
        print(grid[i][j],end=" ")
    print()

