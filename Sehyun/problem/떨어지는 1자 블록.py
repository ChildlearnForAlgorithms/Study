n, m, k = map(int, input().split())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


flag = False

for row in range(1, n):
    for col in range(k - 1, k + m - 1):
        if grid[row][col] == 1:
            for i in range(k - 1, k + m - 1):
                grid[row - 1][i] = 1
            flag = True
            break
    if flag:
        break

if not flag:
    for col in range(k - 1, k + m - 1):
        grid[n - 1][col] = 1

for i in range(n):
    for j in range(n):
        print(grid[i][j], end=" ")
    print()
