import sys


def histogram(F, B, n):
	for i in range(n):
		sum_group, div, div_plus = F[i], 2, 4
		for j in range(i + 1, n):
			MathError[i][j] = MathError[i][j - 1] + (((j - i) * F[j] - sum_group) ** 2) / div
			sum_group += F[j]
			div += div_plus
			div_plus += 2
	dp = [MathError[0]] + [[0] * n for _ in range(B - 1)]
	for k in range(1, B):  # k개로 나눈 최소값
		for i in range(n):
			dp[k][i] = dp[k - 1][i]
			for j in range(i):
				a = dp[k-1][j]+MathError[j+1][i]
				if dp[k][i] > a:
					dp[k][i] = a
	return round(dp[B-1][n-1],3)


B, n = map(int, input().split())
# 최대그룹 수 B, 빈도수의 개수 n
F = [int(sys.stdin.readline()) for _ in range(n)]
MathError = [[0] * n for _ in range(n)]
print(histogram(F, B, n))
'''
알고리즘 분석
먼저, 각 그룹의 오차값을 간단하게 나타내보니
A = (b - a) ** 2 / 2
B = A + (2 * c - b - a) ** 2 / 6
C = B + (3 * d - c - b - a) ** 2 / 12
D = C + (4 * e - d - c - b - a) ** 2 / 20
E = D + (5 * f - e - d - c - b - a) ** 2 / 30
와 같은 형식으로 나타났고 이를 이용하여 먼저 각 그룹의 오차값 테이블을 만들어 주었다.
1개의 그룹으로 i까지 나눴을 때의 값은 오차값 테이블의 [0][i]의 값이고
B개의 그룹으로 i까지 나눴을 때의 값은 dp[k][i] = min([dp[k-1][j] + MathError[j+1][i] For j in range(i)]+[dp[k - 1][i])이다.
이를 계산해보면 i까지 n개의 그룹으로 나누었을 때의 최소 값이 나오고
답은 dp[B-1][n-1]이 된다.
수행시간은 오차값 테이블을 만드는데에 Cn^2의 시간이 걸리고
답을 구하는데에 CBn^2의 시간이 걸렸으므로
O(Bn^2)이다.

'''