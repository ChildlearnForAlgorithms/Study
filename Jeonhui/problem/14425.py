import sys

N, M = map(int, sys.stdin.readline().split())
input_set = [sys.stdin.readline() for _ in range(N)]
input_list = [sys.stdin.readline() for _ in range(M)]
res = 0
for string in input_list:
    if string in input_set:
        res += 1
print(res)