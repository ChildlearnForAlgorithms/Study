import sys


def bfs(x, y):
    global cnt, n
    if visit[x][y] == 0:
        return False
    cnt += 1
    visit[x][y] = 0
    if x + 1 < n and M[x + 1][y] != '0' and visit[x + 1][y]:
        bfs(x + 1, y)
    if y + 1 < n and M[x][y + 1] != '0' and visit[x][y + 1]:
        bfs(x, y + 1)
    if x > 0 and M[x - 1][y] != '0' and visit[x - 1][y]:
        bfs(x - 1, y)
    if y > 0 and M[x][y - 1] != '0' and visit[x][y - 1]:
        bfs(x, y - 1)
    return True


n = int(sys.stdin.readline())
M = [sys.stdin.readline().rstrip() for _ in range(n)]
visit = [[1] * n for _ in range(n)]
res = []
for i in range(n):
    for j in range(n):
        cnt = 0
        if M[i][j] == '1':
            if bfs(i, j):
                res.append(cnt)
print(len(res))
print("\n".join(map(str, sorted(res))))
