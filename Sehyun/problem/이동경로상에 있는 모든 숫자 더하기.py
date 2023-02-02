n, t = map(int, input().split())
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
dir_num = 0
x, y = n // 2, n // 2
state = input()
grid = []
for _ in range(n):
    lst = list(map(int, input().split()))
    grid.append(lst)
cnt = grid[x][y]


def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n


for i in range(t):
    if state[i] == 'R':
        dir_num = (dir_num + 1) % 4
    elif state[i] == 'L':
        dir_num = (dir_num - 1 + 4) % 4
    elif state[i] == 'F':
        nx, ny = x + dx[dir_num], y + dy[dir_num]
        if in_range(nx, ny):
            x, y = nx, ny
            cnt += grid[x][y]

print(cnt)
