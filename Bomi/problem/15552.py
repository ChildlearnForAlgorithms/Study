import sys

T_num = int(input())

for i in range(1, T_num+1):
	tc1, tc2 = map(int, sys.stdin.readline().split())
	sum = tc1 + tc2
	print(sum)