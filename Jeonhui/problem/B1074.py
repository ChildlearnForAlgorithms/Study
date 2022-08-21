import sys


def visit(n, r, c):
    global res
    if n == 0:
        return 0
    if r < n // 2 and c < n // 2:
        return visit(n // 2, r, c)
    elif r < n // 2 <= c:
        res += n // 2 * n // 2
        return visit(n // 2, r, c - n // 2)
    elif r >= n // 2 > c:
        res += n // 2 * n // 2 * 2
        return visit(n // 2, r - n // 2, c)
    elif r >= n // 2 and c >= n // 2:
        res += n // 2 * n // 2 * 3
        return visit(n // 2, r - n // 2, c - n // 2)


N, R, C = map(int, sys.stdin.readline().split())
N = pow(2, N)
res = 0
visit(N, R, C)
print(res)
