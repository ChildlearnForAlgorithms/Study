n, r, c = map(int, input().split())
x, y = r - 1, c - 1
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

dxs, dyx = [-1, 1, 0, 0], [0, 0, -1, 1]

max_num = grid[x][y]
curr_x, curr_y = x, y
num_lst = []
num_lst.append(max_num)

def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n

while True:
    flag = False
    for dx, dy in zip(dxs, dyx):
        nx, ny = curr_x + dx, curr_y + dy
        if in_range(nx,ny) and max_num < grid[nx][ny]:
            max_num = grid[nx][ny]
            curr_x, curr_y = nx, ny
            num_lst.append(max_num)
            flag = True
            break
    if flag == False:
        break
for elem in num_lst:
    print(elem, end=" ")