import sys

N, L = map(int, sys.stdin.readline().split())
cnt = 0
for i in range(1, L):
    cnt += i
if N < cnt or L > 100:
    L = -1
while L != -1 and (N - cnt) % L != 0:
    cnt += L
    L += 1
    if N < cnt or L > 100:
        L = -1
        break
if L == -1:
    print(-1)
else:
    for i in range(L):
        print((N - cnt) // L + i, end=" ")
