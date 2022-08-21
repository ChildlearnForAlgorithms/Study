import sys

n = int(sys.stdin.readline())
maxN = 0
numbers = []
for i in range(n):
    num = int(sys.stdin.readline())
    num = num - 1
    numbers.append(num)
    if maxN < num:
        maxN = num
P = [1, 1, 1]
for i in range(3, maxN + 1):
    P.append(P[i - 2] + P[i - 3])
for i in range(n):
    print(P[numbers[i]])
