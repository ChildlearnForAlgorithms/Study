n, t = map(int, input().split())
r, c, dir = input().split()
r, c = int(r) - 1, int(c) - 1
dx, dy = [0, 1, -1, 0], [1, 0, 0, -1]


def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n


map = {
    'U': 2,
    'D': 1,
    'R': 0,
    'L': 3
}

dir_num = map[dir]

for i in range(n):
    nx, ny = r + dx[dir_num], c + dy[dir_num]
    if not in_range(nx, ny):
        dir_num = 3 - dir_num
    else:
        r, c = nx, ny
    print(r + 1, c + 1)

print(r + 1, c + 1)
