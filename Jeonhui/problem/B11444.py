import sys


def arrayPower(a, b):
    return [
        [(a[0][0] * b[0][0] + a[0][1] * b[1][0]) % 1000000007, (a[0][0] * b[0][1] + a[0][1] * b[1][1]) % 1000000007],
        [(a[1][0] * b[0][0] + a[1][1] * b[1][0]) % 1000000007, (a[1][0] * b[0][1] + a[1][1] * b[1][1]) % 1000000007]]


def fibo(a, n):
    if n == 1:
        return a
    x = fibo(a, n // 2)
    if n % 2 == 1:
        return arrayPower(arrayPower(x, x), a)
    else:
        return arrayPower(x, x)


gx = []
n = int(sys.stdin.readline())
a = fibo([[1, 1], [1, 0]], n)
res = [[a[0][0] * 1 + a[0][1] * 0], [a[1][0] * 1 + a[1][1] * 0]]
print(res[1][0] % 1000000007)
