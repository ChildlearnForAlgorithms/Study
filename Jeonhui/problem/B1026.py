import sys

n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
A = sorted(A)
B = sorted(B, key=lambda x: -x)
res = [x * y for x, y in zip(A, B)]
print(sum(res))
