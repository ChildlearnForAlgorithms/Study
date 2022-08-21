import sys

x = {}
y = {}


def backtrack(k):
    global MP
    if k > n - 1:
        return
    if len(x) == len(y):
        sum_start = 0
        sum_link = 0
        for a in x.keys():
            for q in x.keys():
                sum_start += x[a][q]
        for b in y.keys():
            for q in y.keys():
                sum_link += y[b][q]
        if MP > abs(sum_start - sum_link):
            MP = abs(sum_start - sum_link)
        return
    x[k] = A[k]
    y.pop(k)
    backtrack(k + 1)
    y[k] = A[k]
    x.pop(k)
    backtrack(k + 1)


n = int(sys.stdin.readline())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
MP = 100 * n * n
for i in range(n):
    y[i] = A[i]
backtrack(0)
print(MP)
