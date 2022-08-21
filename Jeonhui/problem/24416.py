import sys


def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


def fibonacci(n):
    cnt = 0
    f = [0] * (n)
    f[0], f[1] = 1, 1
    for i in range(2, n):
        f[i] = f[i - 1] + f[i - 2]
        cnt += 1
    return cnt


n = int(sys.stdin.readline())
print(fib(n), fibonacci(n))
