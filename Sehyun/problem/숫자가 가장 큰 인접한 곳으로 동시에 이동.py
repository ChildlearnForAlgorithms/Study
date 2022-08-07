n, m, t = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
count = [[0] * n for _ in range(n)]



def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


def move(x, y):
    max = 0
    max_pos=(0,0)
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and grid[nx][ny] > max:
            max = grid[nx][ny]
            max_pos=(nx,ny)
    return max_pos

next_count = [[0] * n for _ in range(n)]
def cnt(x,y):
    get_pos_x,get_pos_y=move(x,y)
    next_count[get_pos_x][get_pos_y]+=1
def move_all():
    for i in range(n):
        for j in range(n):
            next_count[i][j]=0
    for i in range(n):
        for j in range(n):
            if count[i][j]==1:
                cnt(i,j)
    for i in range(n):
        for j in range(n):
            count[i][j]=next_count[i][j]

def remove_multiple():
    for i in range(n):
        for j in range(n):
            if count[i][j]>=2:
                count[i][j]=0
def simulate():
    move_all()
    remove_multiple()

for _ in range(m):
    r,c=map(int,input().split())
    count[r-1][c-1]=1

for _ in range(t):
    simulate()

cnt=0
for i in range(n):
    for j in range(n):
        if count[i][j]==1:
            cnt+=1
print(cnt)