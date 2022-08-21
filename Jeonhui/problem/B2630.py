import sys


def check(arr, x, y, n):
    global res
    for i in range(y, y + n):
        for j in range(x, x + n):
            if arr[y][x] != arr[i][j]:
                return False
    if arr[y][x] == 0:
        res[0] += 1
    else:
        res[1] += 1
    return True


def q(arr, x, y, n):
    if n == 0:
        return

    if check(arr, x, y, n):
        return
    else:
        q(arr, x, y, n // 2)
        q(arr, x + n // 2, y, n // 2)
        q(arr, x, y + n // 2, n // 2)
        q(arr, x + n // 2, y + n // 2, n // 2)


n = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
res = [0, 0]
q(paper, 0, 0, n)
print(res[0])
print(res[1])
