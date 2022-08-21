import sys


def NandM(k):
    if k >= m:
        print(" ".join(map(str, x)))
        return
    for i in range(1, n + 1):
        if k == 0 or (k > 0 and x[k - 1] <= i):
            x[k] = i
            NandM(k + 1)


n, m = map(int, sys.stdin.readline().split())
x = [0] * m
NandM(0)
