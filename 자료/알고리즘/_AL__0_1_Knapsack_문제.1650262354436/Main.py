import sys


def fraction_knapsack(i, size):
	pv, sv = 0, 0
	for j in range(i, n):
		if sv + WP[j][0] >= size:
			pv += (WP[j][1] / WP[j][0]) * (size - sv)
			sv += (size - sv)
			break
		sv += WP[j][0]
		pv += WP[j][1]
	return pv


def knapsack(i, size):
	global MP
	if i >= n or size <= 0:
		return
	pv, sv = 0, 0
	for j in range(i):
		if x[j]:
			sv += WP[j][0]
			pv += WP[j][1]
	if WP[i][0] <= size:
		B = fraction_knapsack(i + 1, size - WP[i][0])
		if MP < pv + WP[i][1] + B:
			x[i] = 1
			MP = max(MP, pv + WP[i][1])
			knapsack(i + 1, size - WP[i][0])
	B = fraction_knapsack(i + 1, size)
	if MP < pv + B:
		x[i] = 0
		knapsack(i + 1, size)


MP = 0
K = int(sys.stdin.readline())
n = int(sys.stdin.readline())
weight = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split()))
WP = [[w, p] for w, p in zip(weight, price)]
WP.sort(key=lambda wp: -wp[1] / wp[0])
x = [0] * n
knapsack(0, K)
print(MP)